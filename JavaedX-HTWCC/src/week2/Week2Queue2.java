package week2;

import java.io.*;
import java.util.*;

public class Week2Queue2 {

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

	public static void main(String[] args) throws IOException {
		try (PrintWriter out = newOutput()) {
			FastScanner in = newInput();
			
			//Stack<Integer> ks = new Stack<Integer>();
			LinkedList<Integer> list = new LinkedList<Integer>();
			
			int number_of_operation = in.nextInt();
			int i = 0;
			
			while( i < number_of_operation ){
				
				if("+".equals(in.next())){
					list.add(in.nextInt());
				}else{
					out.println(list.removeFirst());					
				}
				
				i++;
			}
			
//			int j = 0;
//			while(j < list.size()){
//				out.println(list.get(j));
//				j++;
//			}
		}
	}

}
