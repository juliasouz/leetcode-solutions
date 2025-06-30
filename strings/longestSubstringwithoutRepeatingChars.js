var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) {
    return s.length;
  }

  const seenChar = {};
  let left = 0,
    longest = 0;

  for (let right = 0; right < s.length; right++) {
    const currentChar = s[right];
    const previouslySeenChar = seenChar[currentChar];

    if (previouslySeenChar >= left) {
      left = previouslySeenChar + 1;
    }
    seenChar[currentChar] = right;
    longest = Math.max(longest, right - left + 1);
  }
  return longest;
};
