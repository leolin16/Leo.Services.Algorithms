function isPalindrome(s) {
    // s.split("").reverse().join();

    // Sanitize the input string
    s = s.toLowerCase().replace(/[\W_]/g,"") // \W means non-alphanumericunderscorekanji, g means returning all matches
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        if(s[left] !== s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

module.exports = isPalindrome;
