#include "cachelab.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>
#define uint unsigned int
int hit=0,miss=0,eviction=0;

struct CacheStr {
	uint S,E,B;
	uint ***cache;
} Cache;
//初始化cache
void init_Cache(uint s,uint E,uint b)
{
	int i,j;
	Cache.S=1<<s;
	Cache.E=E;
	Cache.B=1<<b;
	//用malloc动态分配内存
	Cache.cache=(uint ***)malloc(Cache.S*sizeof(uint **));
	for(i=0; i<Cache.S; i++) {
		Cache.cache[i]=(uint **)malloc(Cache.E*sizeof(uint *));
	}
	for(i=0; i<Cache.S; i++) {
		for(j=0; j<Cache.E; j++) {
			Cache.cache[i][j]=(uint *)malloc(3*sizeof(uint));
		}
	}
	//初始化每行的有效值、标记位、LRU计数值
	for(i=0; i<Cache.S; i++) {
		for(j=0; j<Cache.E; j++) {
			Cache.cache[i][j][0]=0;//有效值
			Cache.cache[i][j][1]=0;//标志位
			Cache.cache[i][j][2]=0;//LRU计数值
		}
	}
}
//释放内存
void destroy_all()
{
	int i,j;
	for(i=0; i<Cache.S; i++)
		for(j=0; j<Cache.E; j++)
			free(Cache.cache[i][j]);
	for(i=0; i<Cache.S; i++)
		free(Cache.cache[i]);
	free(Cache.cache);
}
//取得有效值
uint get_valid(uint S,uint E)
{
	return Cache.cache[S][E][0];
}
//取得标记位
uint get_tag(uint S,uint E)
{
	return Cache.cache[S][E][1];
}
//取得LRU计数值
uint get_count(uint S,uint E)
{
	return Cache.cache[S][E][2];
}
//找到最近最少使用的一行
uint get_replace(uint S)
{
	uint maxcount=0,replace=0;
	int i;
	for(i=0; i<Cache.E; i++) {
		if(get_count(S,i)>maxcount) {
			maxcount=get_count(S,i);
			replace=i;
		}
	}
	return replace;
}
//修改cache信息
void replace(uint S,uint E,uint tag,_Bool detail)
{
	int i;

	//判断是否需要替换
	if(get_valid(S,E)==1&&get_tag(S,E)!=tag) {
		eviction++;
		if(detail) {
			printf("eviction ");
		}
	}
	//对Cache进行覆盖。
	//L操作不命中需要修改、命中不需要修改，但是修改并不会改变运行结果。
	//S操作无论命中与否都会对数据进行修改。
	//M操作是L、S的结合。
	//于是这里不对命中与否进行区分，一律进行修改。
	Cache.cache[S][E][0]=1;
	Cache.cache[S][E][1]=tag;
	Cache.cache[S][E][2]=0;

	//未访问到的行LRU值加1
	for(i=0; i<Cache.E; i++) {
		if(i!=E) {
			Cache.cache[S][i][2]++;
		}
	}
}
//访问cache
void visit_cache(uint S,uint tag,_Bool detail)
{
	_Bool HitOrNot=0;//标记是否命中
	int i;
	uint hit_item;//记录命中的行
	//遍历组找到匹配的那一行
	for(i=0; i<Cache.E; i++) {
		if(get_valid(S,i)==1&&get_tag(S,i)==tag) { //有效值为1且tag匹配
			HitOrNot=1;
			hit_item=i;
			break;
		}
	}
	if(HitOrNot) {//如果命中
		hit++;
		if(detail) {
			printf("hit ");
		}
		replace(S,hit_item,tag,detail);
	} else {//未命中
		miss++;
		if(detail) {
			printf("miss ");
		}
		replace(S,get_replace(S),tag,detail);
	}

}

void commandlist()
{
	printf("Usage: ./csim-ref [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n");
	printf("options:\n");
	printf("\t-h\t\t打印命名用法\n");
	printf("\t-v\t\t打印详细信息\n");
	printf("\t-s <s>\t\t组索引\n");
	printf("\t-E <E>\t\tcache相联度\n");
	printf("\t-b <b>\t\t块偏移\n");
	printf("\t-t <tracefile>\ttrace文件路径\n");
}


int main(int argc,char *const argv[])
{
	char option,ch_tmp,cmd[1];
	int s=0,E=0,b=0,number;
	uint addr,tag,S;
	_Bool detail=0,error=0;
	FILE *filepath=NULL;

	while((option=getopt(argc,argv,"hvs:E:b:t:"))!=-1) {
		//getopt函数解析命令，此时解析出来的每个部分为字符串
		//atol可以将字符串转换为长整型
		switch(option) {
		case 'h':
			commandlist();
			break;
		case 'v':
			detail=1;
			break;
		case 's':
			s=(int)atol(optarg);
			if(s<=0) {
				error=1;
				printf("csim: error -s %d\n",s);
			}
			break;
		case 'E':
			E=(int)atol(optarg);
			if(E<=0) {
				error=1;
				printf("csim: error -E %d\n",E);
			}
			break;
		case 'b':
			b=(int)atol(optarg);
			if(b<=0) {
				error=1;
				printf("csim: error -b %d\n",b);
			}
			break;
		case 't':
			filepath=fopen(optarg,"r");
			if(filepath==NULL) {
				error=1;
				printf("csim: error -t %s\n",optarg);
			}
			break;
		default:
			error=1;
			break;
		}
	}
	//测试
	//printf("参数：%d %d %d %d\n",detail,s,E,b);
	if(error==1) { //存在输入错误
		//输出命令手册,结束运行
		commandlist();
		return 0;
	}
	//初始化Cache
	init_Cache(s,E,b);
	//读取trace文件，按行处理
	while(fscanf(filepath,"%s%x%c%d",cmd,&addr,&ch_tmp,&number)!=EOF) {
		if(detail) {
			//输出trace中的指令行
			printf("%c %x%c%d ",cmd[0],addr,ch_tmp,number);
		}
		if(cmd[0]!='I') {
			tag=addr>>(s+b);
			S= (((1<<s)-1))&(addr>>b);
			if(cmd[0]=='L'||cmd[0]=='S') {
				//不对L、S指令做区分，直接对valid、tag进行修改，执行结果一致
				visit_cache(S,tag,detail);
			} else {
				//M指令=L指令+S指令
				visit_cache(S,tag,detail);
				visit_cache(S,tag,detail);
			}
		}
		if(detail) {
			printf("\n");
		}
	}
	destroy_all();
	printSummary(hit, miss, eviction);
	return 0;
}