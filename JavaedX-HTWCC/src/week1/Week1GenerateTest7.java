package week1;

import java.io.*;
import java.util.*;

public class Week1GenerateTest7 {

	static class FastScanner {
		static BufferedReader br;
		static StringTokenizer st;

		FastScanner(File f) {
			try {
				br = new BufferedReader(new FileReader(f));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		public FastScanner(InputStream f) {
			br = new BufferedReader(new InputStreamReader(f));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	static FastScanner newInput() throws IOException {
		return new FastScanner(new File("input.txt"));
	}

	static PrintWriter newOutput() throws IOException {
		return new PrintWriter("output.txt");
	}
	
	public static int getDevisors(int n){
		int divisors=1;
		//System.out.print("divisors of "+ n + ": ");
		for(int i=1; i <= n/2; i++){
			if(n % i == 0){
				divisors++;
				//System.out.print(i + ", ");
			}
		}
		//System.out.println("");
		
		return divisors;
		
	}
	
	public static LinkedList<Integer> get_primes(int n){
		LinkedList<Integer> pl = new LinkedList<Integer>();
		
		while(n % 2 == 0){
			pl.add(2);
			n = n/2;
		}
		int i = 3;
		while(i <= Math.sqrt(n)){
			while( n % i == 0){
				pl.add(3);
				n = n/i;
			}
			i = i +2;
		}
		
		if(n > 2)
			pl.add(n);
		
		return pl;
	}
	
	public static int get_div(int x){
		
		Map<Integer,Integer> map = new HashMap<Integer,Integer>();
		// code missing for getting div from prime factors
		
		return 0;
	}

	public static void main(String[] args) throws IOException {
		try (PrintWriter out = newOutput()) {
			FastScanner in = newInput();
			
			Stack<Integer> ks = new Stack<Integer>();
			//LinkedList<Integer> list = new LinkedList<Integer>();
			
			int input = in.nextInt();
			int max_div_pointer = 1;
			int max_div = 1;
			
			for(int i=input/2;i<=input;i++){
				int div = getDevisors(i);
				if(max_div < div){
					max_div = div;
					max_div_pointer = i;
				}
				//System.out.println("pointer: "+ i+ ", max_div: "+ max_div + ", div : " + div);
			}
			//System.out.println("max_div: "+ max_div);
			//System.out.println("max_div_pointer: "+ max_div_pointer);
			//System.out.println(1 + input - max_div_pointer);
			out.println(1 + input - max_div_pointer);
			
		}
	}

}
