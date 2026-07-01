bool isPalindrome(int x) {
    long int original = x;
    long int ans = 0;
    if (x>=0){
        while (x != 0) {
            int rev = x % 10;
            ans = ans * 10 + rev;
            x = x / 10;
        }
        if(original==ans){
            return true;
        }
        else {
            return false;
        }
    }
    else{
        return false;
    }
}