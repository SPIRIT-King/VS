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
	struct msgbuf Snd_Buf = {522, -1, 0};
	struct msgbuf Rcv_Buf;
	key_t key = ftok(".", 22);
	int Msg_ID = msgget(key, IPC_CREAT|0777);
	if (Msg_ID == -1) {
		printf("Msg create failure!\n");
	}
	int index = 0;
	srand(time(NULL));
	while (index < 101) {
		int nread = msgrcv(Msg_ID, &Rcv_Buf, sizeof(Rcv_Buf) - sizeof(long), 2, 0);
			
		int rps_02 = rand()%3;
		Snd_Buf.rps = rps_02;
		int nsnd = msgsnd(Msg_ID, &Snd_Buf, sizeof(Snd_Buf) - sizeof(long), 0);
		
		index++;
	}	
	return 0;
}

