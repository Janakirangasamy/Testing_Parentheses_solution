class Solution {
    public boolean isValid(String s) {
      Stack<Character> symbols = new Stack<>();
      for(char c : s.tocharArray()) {
          if(c == '(' || c=='{' || c=='['){
              symbols.push(c);
          }
          else if (c==')' && !symbols.isEmpty() && symbols.peek()= '('){
              symbols.pop();
          }
          else if (c=='}' && !symbols.isempty() && symbols.peek()= '{'){
              symbols.pop();
          }
          else if (c==']' && !symbols.isempty() && symbols.peek()= ']'){
              symbols.pop();
          }
          else {
              return false;
          }
      } 
       return symbols.isEmpty(); 
    }
}

scenario 1: Multiple open brackets must be closed with same number of and same type of brackets

  Test case 1: Input : s="((()))"
               Output:True
  Test case 2: Input : s="((())"
               Output:False

scenario 2: Different type of brackets must be closed with same order and same type of brackets

  Test case 1: Input : s="[([]{})[(){}]]"
               Output:True
  Test case 2: Input : s="[([]{})[(){}]]]"
               Output:False

scenario 3: Every Open brackets has corresponding close brackets with same type

  Test case 1: Input : s="([])"
               Output:True
  Test case 2: Input : s-"({"
               Output:False
