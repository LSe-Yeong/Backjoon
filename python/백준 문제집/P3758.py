def update_p(logs,n,k):
    s_sum=[0 for j in range(n+1)]
    scores=[[0 for j in range(k+1)] for m in range(n+1)]
    time=[0 for j in range(n+1)]
    count=[0 for j in range(n+1)]
    second=1
    
    for t,p,s in logs:
        if(s>scores[t][p]):
            s_sum[t]+=(s-scores[t][p])
            scores[t][p]=s
        time[t]=second
        second+=1
        count[t]+=1
    
    teams=[]
    
    for i in range(1,n+1):
        teams.append((i,s_sum[i],count[i],time[i])) 
    
    return teams
                    

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n,k,t,m = map(int,sys.stdin.readline().split())
    
    logs=[]
    for i in range(m):
        team, problem, score = map(int,sys.stdin.readline().split())
        logs.append((team,problem,score))
    team_log = update_p(logs,n,k)
    team_log.sort(key=lambda x:(-x[1],x[2],x[3]))
    
    for i in range(len(team_log)):
        if(team_log[i][0]==t):
            print(i+1)
            break
    
    
    