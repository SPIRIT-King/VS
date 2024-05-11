#include<stdio.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<stdlib.h>
#include<string.h>

struct msgbuf {   
	long msgtype;
	int rps;
	int limit_time;
};//消息缓冲区

int result[105];//保存玩家1和玩家2的结果
int player_01_info[105];//保存玩家1的信息
int player_02_info[105];//保存玩家2的信息

int main () {
	char *apt[] = {
		"rock",
		"scissors",
		"papper"
	};

	key_t key_01 = ftok(".", 21);
	key_t key_02 = ftok(".", 22);
	int Msg_ID_01 = msgget(key_01, IPC_CREAT|0777);
	int Msg_ID_02 = msgget(key_02, IPC_CREAT|0777);
	// 定义3个消息缓冲区，用于存储消息
	struct msgbuf Snd_Buf_01 = {1,-1, 1};
	struct msgbuf Rcv_Buf_01;
	struct msgbuf Snd_Buf_02 = {2,-1, 1};
	struct msgbuf Rcv_Buf_02;
	// 定义3个计数器，用于统计数量
	int count_0 = 0;
	int count_1 = 0;
	int count_2 = 0;
	// 定义一个索引，用于记录局次
	int index = 0;

	while (index < 101) {

		// 向队列Msg_ID_01发送消息Snd_Buf_01，接收消息Rcv_Buf_01
		int nsend_01 = msgsnd(Msg_ID_01, &Snd_Buf_01, sizeof(Snd_Buf_01)-sizeof(long),0);
		int nread_01 = msgrcv(Msg_ID_01, &Rcv_Buf_01, sizeof(Rcv_Buf_01)-sizeof(long), 521, 0);
        // 向队列Msg_ID_02发送消息Snd_Buf_02，接收消息Rcv_Buf_02
		int nsend_02 = msgsnd(Msg_ID_02, &Snd_Buf_02, sizeof(Snd_Buf_02)-sizeof(long), 0);
		int nread_02 = msgrcv(Msg_ID_02, &Rcv_Buf_02, sizeof(Rcv_Buf_02)-sizeof(long), 522, 0);
		
		int player_01_rps = Rcv_Buf_01.rps;  // 玩家1的结果
		int player_02_rps = Rcv_Buf_02.rps;  // 玩家2的结果

		int cha = player_01_rps - player_02_rps;
		
		int temp;
		if (cha == 0){ //平局
			temp = 0;
			count_0++;
		}
		else if (cha == -1 || cha == 2) { //玩家1获胜
			temp = 1;
			count_1++;
		}
		else {  //玩家2获胜
			temp = 2;
			count_2++;
		}

		int info1 = player_01_rps;
		int info2 = player_02_rps;
		
		result[index] = temp;
		player_01_info[index] = info1;
		player_02_info[index] = info2;

		index++;
		
	}

	printf("比赛结果如下:\n");
	int ret1 = msgctl(Msg_ID_01, IPC_RMID, NULL);
	int ret2 = msgctl(Msg_ID_02, IPC_RMID, NULL);
	if (ret1 == -1 || ret2 == -1) {
		printf("消息队列销毁失败\n");
	}
	for (int i = 0; i < index; i++) {
		int w = result[i];
		char* win;
		if (w == 0) {
			win = "平局";
		}
		else if(w == 1) {
			win = "玩家1";
		}
		else {
			win = "玩家2";
		}
		
		int p1 = player_01_info[i];
		int p2 = player_02_info[i];

		char* player_01 = apt[p1];
		char* player_02 = apt[p2];

		printf("winner: %s, player_01: %s, player_02: %s\n", win, player_01, player_02);
		printf("---------------------------------------------------\n");
	}

	printf("平局的局数: %d\n", count_0);
	printf("玩家1胜的局数: %d\n", count_1);
	printf("玩家2胜的局数: %d\n", count_2);

	if (count_1 == count_2) {
		printf("平局!\n");
	}
	else if (count_1 < count_2) {
		printf("玩家2是赢家\n");
	}
	else {
		printf("玩家1是赢家\n");
	}
	return 0;
}

