#include<stdio.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

struct msgbuf {                                          
	long msgtype;                         
	int rps;                                    
	int limit_time;
};

int main () {
	struct msgbuf Snd_Buf = {521, -1, 0};// 发送消息类型为 521 到消息队列
	struct msgbuf Rcv_Buf;
	key_t key = ftok(".", 21);// key 与 裁判程序里面的一样
	int Msg_ID = msgget(key, IPC_CREAT|0777);
	if (Msg_ID == -1) {
		printf("消息队列创建失败!\n");
	}
	int index = 0;
	srand(time(NULL));
	while (index < 101) {

		// 接收消息
		int nread = msgrcv(Msg_ID, &Rcv_Buf, sizeof(Rcv_Buf) - sizeof(long), 1, 0);    
			
		// 产生随机数，用来模拟接收数据帧的个数
		int rps_01 = rand()%3;

		// 填充发送数据帧
		Snd_Buf.rps = rps_01;
        
		// 发送数据
		int nsnd = msgsnd(Msg_ID, &Snd_Buf, sizeof(Snd_Buf) - sizeof(long), 0);
		
		// 索引加1
		index++;
	}	
	return 0;
}

