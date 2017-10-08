class TickTacToe(object):
    import logging
    
    playerNames = ['','']
    boardData = {'a':['A1', 'A2', 'A3'],'b':['B1', 'B2', 'B3'], 'c':['C1', 'C2', 'C3']}
    highestCount = 0
    gameCount = 0
    aColumnMatched = False
    bColumnMatched = False 
    cColumnMatched = False
    row1Matched = False
    row2Matched = False
    row3Matched = False
    leftToRightCross = False
    rightToLeftCross = False
    isOver = False
    isTied = False
    
    def __init__(self):
        self.setHeighestWordCounts()
        
    def setHeighestWordCounts(self):
        for letter,array in self.boardData.iteritems():
            for value in array:
                strCount = len(value)
                self.highestCount = strCount
    
    def setPlayerNames(self,playerName1, playerName2):
        if(isinstance(playerName1, str) and isinstance(playerName2, str)):
            self.playerNames = [playerName1, playerName2]

    def printBoard(self):
        string = ''
        self.setHeighestWordCounts()
        string = string + self.printTopLine() + '\n'
        string = string + self.drawBorder() + '\n'
        for x in [1,2,3]:
            string = string + self.drawNumberRow(x) + '\n'
            string = string + self.drawBorder() + '\n'
        return raw_input(string)

    def getInitialUserInput(self):
        print 'Please type your position. \nFor example, typing a1 means you take A1\n'
        return self.printBoard()
    
    def getUserInput(self):
        return raw_input('Please type your position.\n')
        
    def printTopLine(self):
        if self.highestCount == 1:
            return '  |  A  |  B  |  C  |'
        elif self.highestCount == 2:
            return '  |  A   |  B   |  C   |'


    def drawBorder(self):
        if self.highestCount == 1:
            return '--|-----|-----|-----|'
        elif self.highestCount == 2:
            return '--|------|------|------|'
        else:
            logging.warning('input was too long!')

    def drawNumberRow(self,rowNumber):
        aValue = self.boardData['a'][rowNumber-1]
        bValue = self.boardData['b'][rowNumber-1]
        cValue = self.boardData['c'][rowNumber-1]
        return '{x} |  {a}  |  {b}  |  {c}  |'.format(x=rowNumber, a=aValue, b=bValue, c=cValue)
    
    def setBoardData(self,input):
        letter = ''
        number = 0
        if(len(input) > 3 or len(input) < 2):
            logging.warning('unexpected input!')
            return False
        elif(input[1].isdigit):
            letter = input[0]
            number = int(input[1]) - 1
            letterExists = letter in self.boardData
            numberExists = len(self.boardData[letter][number]) > 0
            if(letterExists and numberExists):
                self.boardData[letter][number] = self.getCellValue()
        else:
            logging.warning('incorrect input! please make sure to select right cell.')
            return False
        
    def emptyBoardData(self):
        self.boardData = {'a':[' ', ' ', ' '],'b':[' ', ' ', ' '], 'c':[' ', ' ', ' ']}
        
        
    def addGameCount(self):
        self.gameCount += 1
        
    def printTurn(self):
        if(self.gameCount%2 == 0):
            print '\n'+ self.playerNames[1] + '\'s Turn! \n'
        else:
            print '\n'+ self.playerNames[0] + '\'s Turn! \n'
        
    def getCellValue(self):
        if(self.gameCount%2 == 0):
            return 'X'
        else:
            return 'O'
        
    def updateGameStatus(self):
        self.aColumnMatched = self.boardData['a'][0] == self.boardData['a'][1] == self.boardData['a'][2] != ' '
        self.bColumnMatched = self.boardData['b'][0] == self.boardData['b'][1] == self.boardData['b'][2] != ' '
        self.cColumnMatched = self.boardData['c'][0] == self.boardData['c'][1] == self.boardData['c'][2] != ' '
        self.row1Matched = self.boardData['a'][0] == self.boardData['b'][0] == self.boardData['c'][0] != ' '
        self.row2Matched = self.boardData['a'][1] == self.boardData['b'][1] == self.boardData['c'][1] != ' '
        self.row3Matched = self.boardData['a'][2] == self.boardData['b'][2] == self.boardData['c'][2] != ' '
        self.leftToRightCross = self.boardData['a'][0] == self.boardData['b'][1] == self.boardData['c'][2] != ' '
        self.rightToLeftCross = self.boardData['c'][0] == self.boardData['b'][1] == self.boardData['a'][2] != ' '
        
    def printGameStatus(self):
        if(self.aColumnMatched):
            self.printStatus('got all the column A.')
            self.isOver = True
        elif(self.bColumnMatched):
            self.printStatus('got all the column B.')
            self.isOver = True
        elif(self.cColumnMatched):
            self.printStatus('got all the column C.')
            self.isOver = True
        elif(self.row1Matched):
            self.printStatus('got all the row 1.')
            self.isOver = True
        elif(self.row2Matched):
            self.printStatus('got all the row 2.')
            self.isOver = True
        elif(self.row3Matched):
            self.printStatus('got all the row 3.')
            self.isOver = True
        elif(self.leftToRightCross):
            self.printStatus('got the cross from left to right.')
            self.isOver = True
        elif(self.rightToLeftCross):
            self.printStatus('got the cross from right to left.')
            self.isOver = True
        else:
            emptyValueExist = False
            for letter,array in self.boardData.iteritems():
                for value in array:
                    if value == ' ' or value == '':
                        emptyValueExist = True
            if(emptyValueExist):
                self.printBoard()
                self.printTurn()
            else:
                # game was tie
                game.isOver = True
                game.isTied = True
                print 'Game was tie! Great job both!'
                
    def printStatus(self,comment):
        if(self.gameCount%2 == 0):
            print self.playerNames[1] + ' won!! ' + comment
        else:
            print self.playerNames[0] + ' won!! ' + comment
            
    def isCellAvailable(self,cell):
        if(len(input) > 3 or len(input) < 2):
            return False
        letter = cell[0]
        number = int(cell[1]) - 1
        letterExists = letter in self.boardData
        numberExists = len(self.boardData[letter][number]) > 0
        
        if(letterExists and numberExists):
            if(self.boardData[letter][number] == ' '):
                return True
            else:
                return False
        else:
            return False
        
gameStop = False
while gameStop == False:
    playerName1 = raw_input('Welcome to Tick Tac Toe Game! Please type first player\'s name. : ')
    playerName2 = raw_input('Please type second player\'s name. : ')
    initialDic = {'a':['A1', 'A2', 'A3'],'b':['B1', 'B2', 'B3'], 'c':['C1', 'C2', 'C3']}
    inputDic = {'a':[' ',' ',' '],'b':[' ',' ',' '],'c':[' ',' ',' ']}
    game = TickTacToe()
    game.setPlayerNames(playerName1, playerName2)

    firstInput = game.getInitialUserInput()
    if firstInput == 'quit':
        gameAgainInput = raw_input('If you want to play again, please type Yes')
        if(gameAgainInput.lower() == 'yes'):
            continue
        else:
            print 'Thank you for playing Tick Tac Toe Game!'
            break
            gameStop = True
            
    game.emptyBoardData()
    game.setHeighestWordCounts()
    game.setBoardData(firstInput)
    game.updateGameStatus()
    game.printGameStatus()
    game.addGameCount()
    if(game.isOver):
        gameAgainInput = raw_input('If you want to play again, please type Yes')
        if(gameAgainInput.lower() == 'yes'):
            continue
        else:
            print 'Thank you for playing Tick Tac Toe Game!'
            gameStop = True
            
    else:
        # game is not over
        while game.isOver == False:
            cellAvailable = False
            while cellAvailable == False:
                gameInput = game.getUserInput()
                if(gameInput.lower() == 'quit'):
                    game.isOver = True
                    gameStop = True
                    break
                cellAvailable = game.isCellAvailable(gameInput)
                if(cellAvailable):
                    game.setBoardData(gameInput)
            if(game.isOver and gameStop):
                break
                
            game.updateGameStatus()
            game.printGameStatus()
            game.addGameCount()
            
        gameAgainInput = raw_input('If you want to play again, please type Yes')
        if(gameAgainInput.lower() == 'yes'):
            continue
        else:
            print 'Thank you for playing Tick Tac Toe Game!'
            gameStop = True