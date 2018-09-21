nclude <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct _NodeStatInfo {
    char status[10];
    char name[64];
} NodeStatInfo;

int count = 3;

int cluster_info(char *remote_ip,
                 NodeStatInfo ***info,
                 int *node_count)
{
    int i;
    *info = (NodeStatInfo **)malloc(sizeof(NodeStatInfo *) * count);
    for(i = 0; i < count; i++) {
        (*info)[i] = (NodeStatInfo *)malloc(sizeof(NodeStatInfo));
        strcpy((*info)[i]->status, "init");
        sprintf((*info)[i]->name, "node%d", i); 
    }
    *node_count = count;
    return 0;
}
