#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    pid_t pid = fork(); // 创建子进程

    if (pid < 0) { // fork失败
        printf("Fork failed\n");
        return 1;
    } else if (pid == 0) { // 子进程
        printf("子进程PID: %d\n", getpid());
        char *args[] = {"ls", NULL}; // ls命令作为参数传递给execvp
        execvp("ls", args); // 使用execvp执行ls命令
        printf("execvp error\n"); // 如果执行到这里，说明execvp调用出错
        exit(1);
    } else { // 父进程
        printf("父进程PID: %d, 子进程PID: %d\n", getpid(), pid);
        wait(NULL); // 等待子进程结束
        printf("子进程已结束\n");
    }

    return 0;
}