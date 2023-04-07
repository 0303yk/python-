public class demo001 {
    public static void main(String[] args) {
        BigInteger a = new BigInteger("7");
        BigInteger c = new BigInteger("1921");
        BigInteger b = a.pow(2020);
        //BigInteger d = b.mod(c);
        BigInteger result = b.remainder(c);
        //System.out.println(d);
        System.out.println(result);
    }
}
public class demo002 {
    public static void main(String[] args) {
        String a = "astghi";
        String b = "abcdef";
        String c ="stghia";
        String y = "";
        HashMap<String,String> map = new HashMap<>();
        for (int i = 0; i <a.length() ; i++) { map.put(String.valueOf(a.charAt(i)),String.valueOf(b.charAt(i)));}
        for (int j = 0; j < c.length() ; j++) { String s = map.get(String.valueOf(c.charAt(j)));
            y += s;}
        System.out.println(y);

    }
}
public class demo003 {
    public static void main(String[] args) {
        int tili = 10000;
        int count = 0 ;
        boolean b = true;
        while (true){
            if(tili <600&& b){
                break;
            }
            if(b){
                tili-=600;
                b=false;
            }else {
                tili+= 300;
                b = true;
            }
            count++;
        }
        System.out.println(count*60 +tili/10);
    }
}
public class demo004 {
    public static void main(String[] args) {
        int min = 9999999;
        int answer = -1;
        for (int i = 1; i < 101; i++) {
            int x ;
            if(100%i != 0){
                x = 100/i +i +1;
            }else{
                x = 100/i +i;
            }
            if(x<min){
                min = x;
                answer = i ;
            }
        }
        System.out.println(answer);
    }
}

public class demo005 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        int a = 0;int b = 0;int d = 0;
        for (int i = 0; i <s.length() ; i++) {
            char c = s.charAt(i);
            if(c<='Z'&&c>='A') { a++; }
            if(c<='z'&&c>='a') { b++; }
            if(c<='9'&&c>='0') { d++; }
        }
        System.out.println(a);
        System.out.println(b);
        System.out.println(d);
    }
}
public class demo006 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
//        System.out.print(s+" ");
//        while (s/2 > 0){
//            if(s%2 == 1){ s = (s-1)/2;System.out.print(s+" "); }
//            else { s = s / 2;System.out.print(s+" "); }
//        }
        while(s != 0){
            System.out.print(s+" ");
            s/=2;
        }

    }
}


