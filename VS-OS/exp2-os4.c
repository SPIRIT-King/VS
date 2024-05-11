#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>
 
#define N 5
 
//定义一个整型变量readcount，用于记录读操作的次数
int readcount=0;
//定义整型变量a，用于赋值
int a=5;
//定义整型变量b，用于赋值
int b=5;
//定义一个整型数组r，用于存放读操作的值
int r[N]={0,1,2,3,4};
//定义三个信号量，wmutex用于互斥访问写操作，rmutex用于互斥访问读操作，queue用于等待队列
sem_t wmutex,rmutex,queue;
 
 
void delay()
{
	int time = rand() % 10 + 1;          //随机使程序睡眠0点几秒           
	usleep(time * 100000);
}
 
void Reader(void *arg)
{
	int i=*(int *)arg;
	while(a>0)
	{
    	a--;
    	delay();
    	
			//让写者进程排队，读写进程具有相同的优先级 
        	sem_wait(&queue);		
        	//与其他读者进程互斥的访问readcount 
        	sem_wait(&rmutex);		
        	if(readcount==0)
        		//与写者进程互斥的访问共享文件 
        		sem_wait(&wmutex);	
        	readcount++;
        	sem_post(&rmutex);
			//使得写者进程进入准备状态 
        	sem_post(&queue);		
	
			//Reader
        	printf("Reader%d is reading!\n",i);
        	printf("Reader%d reads end!\n",i);
        	
        	//与写者进程互斥的访问readcount 
        	sem_wait(&rmutex);
        	//读取完毕，reader出队 
        	readcount--;
        	if(readcount==0)
        	    //最后一个读者，释放写者锁 
        	    sem_post(&wmutex);
        	sem_post(&rmutex);
    	}	
}
 
void Writer()
{
	while(b>0)
    	{
    		b--;
    		delay();
    		
    		//等待写入操作完成
    		sem_wait(&queue); 
        	//锁定写入操作
    		sem_wait(&wmutex);
    		
    		printf("writer is writing!\n");
        	printf("writer writes end!\n");
    		
        	//解锁写入操作
        	sem_post(&wmutex);
        	//解锁写入操作
        	sem_post(&queue);
    	}
}
 
int main()
{
	int i;
	pthread_t writer,reader[N];
	srand((unsigned int)time(NULL));
	
	//初始化互斥锁 
	sem_init(&wmutex,0,1);
	sem_init(&rmutex,0,1);
	sem_init(&queue,0,1);
	
	//创建线程 
	for(i=0;i<5;i++)
	{
		pthread_create(&reader[i],NULL,(void *)Reader,&r[i]);
	} 
	
	pthread_create(&writer,NULL,(void *)Writer,NULL);
		
	//等待线程结束 
	pthread_join(writer,NULL);
	
	//销毁互斥锁 
	sem_destroy(&rmutex);
	sem_destroy(&wmutex);   
	sem_destroy(&queue); 
	
	return 0;
} 