#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define IPADDR "192.168.247.135"  // ifconfig查看IP地址
#define PORT 8988

int main(void){
    // 第一步：先socket打开文件描述符(类似open的文件描述符)
    // 如果错误返回-1
	int socketfd=socket(AF_INET,SOCK_STREAM,0);
     	if (-1==socketfd)
    	{
        	printf("Socket Error\n");
            return -1;
    	}

     // 第二步：bind绑定socketfd和当前电脑的IP地址&端口号
     struct sockaddr_in serveraddr={0};
     serveraddr.sin_family=AF_INET;     // IPv4
     serveraddr.sin_addr.s_addr=inet_addr(IPADDR);
     serveraddr.sin_port=htons(PORT);   // 端口
     // 正确返回0，错误返回-1
    int ret=bind(socketfd,(const struct sockaddr *)&serveraddr,sizeof(serveraddr));
    if (ret!=0)
    {
        printf("Bind Error");
        return -1;
    }
    // 第三步：建立监听
    ret=listen(socketfd,10);
    if (ret!=0)
    {
        printf("Listen Error");
        return -1;
        }
    // 第四步：阻塞等待客户端链接
    struct sockaddr_in clientaddr={0};
    socklen_t len=0;
    // 参数2：保存链接进来的客户端信息,accept函数会使程序阻塞在这
    ret=accept(socketfd,&clientaddr,&len);
    printf("Server Running\n");
}