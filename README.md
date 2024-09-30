- Practice Python by implementing ADTs, basic algorithms
- Practice problems
- ???

- [ ] Prim's
- [ ] Kruskal's
- [ ] Coin change problem
- [ ] Maximum subarray
- [ ] Crystal ball
- [ ] AVL
- [ ] Red black

# NppExec scripts
## run_lua
```
SET interpreter = C:\sourcecode\lua-5.4.2_Win64_bin\lua54.exe
SET exec = "$(interpreter)" "$(FULL_CURRENT_PATH)"
NPP_SAVE
$(exec)
if $(EXITCODE) != 0 goto exit
NPP_CONSOLE 1
NPP_RUN cmd /C "cmd /C $(exec) && pause"
:exit
```
## run_python
```
C:\Users\usern\AppData\Local\Programs\Python\Python312\python.exe "$(FILE_NAME)"
```
