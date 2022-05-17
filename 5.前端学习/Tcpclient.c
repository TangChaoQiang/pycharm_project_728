#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define SERVERADDR "127.0.0.1"  // 服务器IP
#define SERVERPORT 4399

int main(void){
    // 第一步：先socket打开文件描述符(类似open的文件描述符)
    // 如果错误返回-1
    int socketfd=socket(AF_INET,SOCK_STREAM,0);
    if (-1==socketfd)
     {
         printf("Socket Error\n");
         return -1;
     }
        
    // 第二步：connect链接服务端
     struct sockaddr_in server={0};
     server.sin_family=AF_INET;
     server.sin_port=htons(SERVERPORT);
     server.sin_addr.s_addr=inet_addr(SERVERADDR);
     int ret=connect(socketfd,(const struct sockaddr *)&server,sizeof(server));
     if (ret!=0)
     {
         printf("Connect Error\n");
        return -1;
     }
     printf("Connect Success\n");
}