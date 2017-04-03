package week2;

import java.io.*;
import java.util.*;

public class Week2Snowmen6 {

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

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		try (PrintWriter out = newOutput()) {
			FastScanner in = newInput();
			
			ArrayList<Stack<Integer>> snowManLists = new ArrayList<Stack<Integer>>();
			LinkedList<Long> snowmanTotalMass = new LinkedList<Long>();
			
			
			int number_of_operation = in.nextInt();
			int i = 1;
			
			int a = in.nextInt();
			int b = in.nextInt();
			
			Stack<Integer> st = new Stack<Integer>();
			st.add(b);
			//System.out.println("st: " + st);
			snowManLists.add((Stack<Integer>) st.clone());
			
			snowmanTotalMass.add(Long.valueOf(b));
			
			//System.out.println("snowman list: "  + snowManLists.get(0));
			while(i<number_of_operation){
				
				//System.out.println(i);
				int act = in.nextInt();
				int desc = in.nextInt(	);
				
				
				if(act == 0){
					Stack<Integer> topEleStack = new Stack<Integer>();
					topEleStack.add(desc);
					snowManLists.add(topEleStack);
					snowmanTotalMass.add(Long.valueOf(desc));		
					
				}
				else if(desc == 0){
					Stack<Integer> topEleStack = new Stack<Integer>();
					topEleStack.addAll(snowManLists.get(act-1));
					
					int topElementToPop = 0;
					if (topEleStack.size() > 0)
						topElementToPop = topEleStack.pop();
					snowmanTotalMass.add(snowmanTotalMass.get(act-1) - topElementToPop);
					
					//System.out.println(topEleStack);
					snowManLists.add(topEleStack);					
				}else{
					snowmanTotalMass.add(snowmanTotalMass.get(act-1) + desc);
					Stack<Integer> topEleStack = new Stack<Integer>();
					topEleStack.addAll(snowManLists.get(act-1));
					topEleStack.add(desc);
					//System.out.println(topEleStack);
					snowManLists.add(topEleStack);
				}
				
				i++;
			}
			
			
			//System.out.println(snowmanTotalMass);
			//System.out.println(snowManLists);
			
			Long totalMass = (long) 0;
			int j = 0;
			while(j < snowmanTotalMass.size()){
				totalMass = totalMass + snowmanTotalMass.get(j);
				j++;
			}
			out.println(totalMass);
			
		}
	}

}
