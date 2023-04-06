/*
6种作物 2种起初数量 4种杂交数量 6目标种子类型
第i种作物种植时间 5 3 4 6 4 9
已拥有的种子类型1 2
第一列和第二列杂交可获得第三列的品种
1 2 3
1 3 4
2 3 5
4 5 6
*/
import java.util.Scanner;
// 1:无需package
// 2: 类名必须Main, 不可修改

public class Main {
    static int n;//作物总类数
    static int m;//初始拥有作物种类数
    static int k;//方案数
    static int t;//目标作物编号
    static int total_time = 0;//总时长
    static int[] time;//作物成熟时间
    static int[][] task;//方案
    static int[] flag;//得到的种子作物种类情况
    static void dfs(int t){
        for (int i = 0; i < k; i++) {
            if(task[i][2]==t){
                if(flag[task[i][0]]!=1||flag[task[i][1]]!=1){
                    total_time += Math.max(time[task[i][0]],time[task[i][1]]);
                    //System.out.println(i);
                    if(flag[task[i][0]]!=1){
                        dfs(task[i][0]);
                    }
                    if(flag[task[i][1]]!=1){
                        dfs(task[i][1]);
                    }
                    flag[t]=1;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        t = sc.nextInt();
        time = new int[n+1];
        task = new int[k][3];
        flag = new int[n+1];
        int p;
        for (int i = 1; i <= n; i++) {
            time[i] = sc.nextInt() - 1;
        }
        for (int i = 1; i < m+1; i++) {
            p = sc.nextInt();
            /*flag[p] = 1;*/
        }
        for(int i = 0;i < k; i++){
            for(int j = 0;j < 3;j++){
                task[i][j] = sc.nextInt();
            }
        }
        flag[t] = 1;
        dfs(t);
        System.out.println(total_time);
    }
}
}
