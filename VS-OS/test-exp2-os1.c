#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
 
int main(){
        pid_t pid;      //parent_id
        pid_t cid;      //child_pid
        printf("Before fork Process id: %d\n", getpid());
        cid = fork();
        if(cid==0){     //子进程会执行的代码
                printf("Child process id(my parent id is %d): %d\n", getppid(), getpid());
                for(int i=0; i<3; i++){
                        printf("Hello %d\n", i);
                }
        }else {         //父进程会执行的代码
                printf("Parent process id: %d\n", getpid());
                for(int i=0; i<3; i++){
                        printf("World %d\n", i);
                }
        }
        printf("After fork, Process id: %d\n", getpid());
        return 0;
}