import java.util.Scanner;
// 1:无需package
// 2: 类名必须Main, 不可修改
static boolean[] flag; //标记该种植是否拥有
static int[][] line; //记录方案
static int[] time; //该种子种植所需要的时间
static int[] maxTime; //该种子通过杂交得到的时间
static int[] res; //该种子最终合成需要的时间，用于dfs
static int T;//目标种子的编号

private static void getInputStreamData() {
    Scanner scan = new Scanner(System.in);

    //第一行的数据
    int N = scan.nextInt(); //作物种类总数
    int M = scan.nextInt(); //我们初始拥有的种子类型数量
    int K = scan.nextInt(); //可以杂交的方案数量
    int T = scan.nextInt(); //T就是目标种子的编号，我们要拿到得到这个种子的最短的杂交时间

    init(N,M,K,T);

    //第二行的数据,从1开始，通过编号找到耗时
    for(int i = 1;i<=N;i++) {
        time[i] = scan.nextInt();
    }

    //第三行数据
    for(int i = 0 ;i<M;i++) {
        int seed = scan.nextInt();
        flag[seed] = true; //标记拥有该种子
    }

    //第四行数据
    for(int i = 0;i<K;i++){
        // C = A + B
        line[i][0] = scan.nextInt(); // A
        line[i][1] = scan.nextInt(); // B
        line[i][2] = scan.nextInt(); // C
        //该种子，也就是C，得到它需要耗费的时间
    /*
      这里不用hash表记录的原因是，C可以由多种不同的方案得到，如果用hash表，hash表只会记录最新一次的方案
      所以这里通过i来记录是方案编号
    */
        maxTime[i] = Math.max( time[ line[i][0] ] ,time[ line[i][1] ] );
    }
    scan.close();
}

private static void init(int N,int M,int K,int t) {
    flag = new boolean[N+1]; //使得下标可以==N
    line = new int[K][3]; // line[i][0] = A,line[i][1] = B,line[i][2] = C;
    time = new int[N+1];
    maxTime = new int[K]; //maxTime记录该方案所需要的最大时间，也就是C = A+B所需要的最大时间
    res = new int[N+1]; //得到该种子的总耗时
    T = t;
}

public static void main(String[] args) {
    //拿数据
    getInputStreamData();
    //dfs搜索可行方案
  /*
    我们需要得到种子T，那么就要拿到种子T的最大耗时，种子T由A和B组成，那么我们拿到A和B的最大耗时
    取二者中最大一个即可。
    因为已经拥有的种子不需要耗时，也就是耗时0，所以我们可以得出递归条件就是
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //在此输入您的代码...
        scan.close();
    }
}
