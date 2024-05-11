#include<iostream>
#include<thread>
#include<condition_variable>
#include<mutex>

using namespace std;

mutex mtx; //互斥信号量,用于实现互斥的访问临界区
condition_variable buf_full; //条件变量，用于当产品放满缓冲区，将生产者进程阻塞
condition_variable buf_empty; //条件变量，用于当缓冲区为空时，将消费者进程堵塞
int freebuf = 5; //表示空闲缓冲区个数
int prd_sum = 10; //表示总共要生产的产品总数
int curprd = 0; //表示当前的产品数

void producing(int i) {
	unique_lock<mutex> lock(mtx); //生产者线程获取锁，将锁与互斥锁对象mtx相关联
	while (freebuf <= 0) { //这里的freebuf <= 0就是条件变量buf_full的条件
		cout << "当前缓冲区已满，无法将产品放入缓冲区..." << endl;
		buf_full.wait(lock); //当缓冲区满时，使用while循环使进程进入等待状态
	} 
	freebuf--; //产品放入缓冲区中，空闲缓冲区个数减1
	curprd++; //当前产品个数加1
	cout << "第" << i << "个产品已经放入缓冲区" << endl;
	buf_empty.notify_all(); //缓冲区中已有产品，唤醒消费者进程
	lock.unlock(); //将当前生产者进程占用的临界区解锁，此时缓冲区中有物品，消费者可以访问
}

void producer() {
	for (int i = 0; i < prd_sum; i++) {
		cout << "现在正在生产第" << i + 1 << "个产品" << endl;
		producing(i + 1);
	}
}

void consuming(int i) {
	unique_lock<mutex> lock(mtx); //锁定缓冲区，防止生产者进程访问
	while (curprd <= 0) { //这里的curprd <= 0就是条件变量buf_empty的条件
		cout << "当前没有产品可供消耗" << endl;
		buf_empty.wait(lock); //当前缓冲区中没有产品，故将消费者进程堵塞
	}
	freebuf++; //消费者消耗一个产品，缓冲区数量加1
	curprd--; //产品数量减1
	cout << "消费者消耗第" << i + 1 << "个产品" << endl;
	buf_full.notify_all();
	lock.unlock(); //将当前消费者进程占用的临界区解锁，此时缓冲区中没有满，生产者可以访问
}

void consumer() {
	for (int i = 0; i < prd_sum - freebuf; i++)
		consuming(i);
}

int main() {
	thread produce(producer);
	thread consume(consumer);
	produce.join();
	consume.join();
	cout << "生产者已完成生产任务" << endl;
}

