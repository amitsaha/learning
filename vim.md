## Tips

**Cursor movement**

- Move to the line below: `j`
- Move the line above: `k`
- Move to the character on the right: `l`
- Move to the character on the left: `h`
- Move forward to the start of the next word: `w`
- Move forward to the end of the next word: `e`
- Move backward to the start of the previous word: `b`
- Move backward to the end of the previous word: `ge`
- Jump to the beginning of a line: `0`
- Jump the end of a line: `$`


**Line search**

`f<c>` to go the next occurence of `c`, `;` to repeat this search, `,` to repeat the search in backward direction
`F<c>` to go the previous occurence of `c`, `;` to repeat this search, `,` to repeat the search in forward direction

**Changing a word at n positions**

- Search for the word
- `cgn` - change it
- Press the `.` key to change the next, `n` to skip it

**Recording and playing macros**

- Start macro recording: `q<key>` where key is the register you want to store the macro in
- `<perform actions>`. One point to note here is to make your steps so that you start from the beginning of a line.
- Press `q` to save
- To apply the macro on a line: `@<key>`
- To apply the macro to a selection:
  - Visually select the area
  - `:'<,'> normal @<key>`


**Switch case**

- Select the character, word
- Press `~`.

**Replace character**

- Select
- `Shift+R`

**Move block of text**

- Left: `<<`
- Right: `>>`

**Delete**

- Delete till a character on the current line: `dt<character>` 
- Delete current word: `diw`
- Delete text between quotes: `di"`

**Miscellaneous movements**

- `zz` to center the current line to the center
- `G` to go the last line of the document
- `gg` to go the first line of the document
- `H` to move to the top of the screen
- `M` to move to the middle of the screen
- `L` to move to the bottom of the screen

## External Resources

- [vim tips and tricks](https://www.rosehosting.com/blog/vim-tips-and-tricks/)
- [vi/vim cheat sheet](http://www.viemu.com/vi-vim-cheat-sheet.gif)
- [vim cheat sheet](https://vim.rtorr.com/)
- [Search and Replace](http://vim.wikia.com/wiki/Search_and_replace)
- [Visual block mode](http://vimcasts.org/transcripts/22/en/)
- [Habit breaking, Habit Making](http://vimcasts.org/blog/2013/02/habit-breaking-habit-making/)
- [You don’t need more than one cursor in vim
](https://medium.com/@schtoeffel/you-don-t-need-more-than-one-cursor-in-vim-2c44117d51db)
