function weighted_random() {
    var options = [
        {name:"Pele", weight: 548},
        {name:"Zinedine", weight: 1019},
        {name:"Ronaldinho", weight: 678},
        {name:"Yashin", weight: 7008},
        {name:"Garrincha", weight: 1610},
        {name:"Baggio", weight: 8410},
        {name:"Baresi", weight: 13316},
        {name:"Basten", weight: 13775},
        {name:"Best", weight: 1815},
        {name:"Eusebio", weight: 768},
        {name:"Xavi", weight: 4597},
        {name:"Zanetti", weight: 10012},
        {name:"Cannavaro", weight: 5056},
        {name:"Stoichkov", weight: 4404},
        {name:"Pirlo", weight: 11097},
        {name:"Maradona", weight: 1151},
        {name:"Ronaldo", weight: 301},
        {name:"Cruyff", weight: 636},
        {name:"Maldini", weight: 1065},
        {name:"Puskas", weight: 1598},
        {name:"Henry", weight: 2496},
        {name:"Alberto", weight: 3566},
        {name:"Gullit", weight: 543},
        {name:"Matthaus", weight: 1736},
        {name:"Cantona", weight: 1644},
        {name:"Giggs", weight: 1536},
        {name:"Nesta", weight: 12682},
        {name:"Rivaldo", weight: 1051},
        {name:"Figo", weight: 4196},
        {name:"Nistelrooy", weight: 16645},
        {name:"Raul", weight: 6947},
        {name:"Moore", weight: 17522},
        {name:"Lineker", weight: 14166},
        {name:"Puyol", weight: 11715},
        {name:"Schmeichel", weight: 12106},
        {name:"Eto", weight: 1490},
        {name:"Shearer", weight: 22318},
        {name:"Desailly", weight: 3357},
        {name:"Pires", weight: 21026},
        {name:"Owen", weight: 12484},
        {name:"Nedved", weight: 12292},
        {name:"Gerrard", weight: 8322},
        {name:"Drogba", weight: 4842},
        {name:"Kaka", weight: 3535},
        {name:"Hagi", weight: 13871},
        {name:"Sanchez", weight: 6222},
        {name:"Butragueno", weight: 3121},
        {name:"Piero", weight: 9511},
        {name:"Bergkamp", weight: 12484},
        {name:"Dalglish", weight: 2853},
        {name:"Beckham", weight: 7398},
        {name:"Scholes", weight: 18581},
        {name:"Seedorf", weight: 9226},
        {name:"Ballack", weight: 5789},
        {name:"Trezeguet", weight: 21478},
        {name:"Shevchenko", weight: 12682},
        {name:"Riquelme", weight: 14851},
        {name:"Sar", weight: 8392},
        {name:"Hierro", weight: 13775},
        {name:"Koeman", weight: 9226},
        {name:"Socrates", weight: 6817},
        {name:"Kluivert", weight: 16576},
        {name:"Carlos", weight: 3995},
        {name:"Klose", weight: 14796},
        {name:"Lahm", weight: 6222},
        {name:"Schweinsteiger", weight: 5707},
        {name:"Laudrup", weight: 21478},
        {name:"Vieira", weight: 1141},
        {name:"Blanc", weight: 6899},
        {name:"Rush", weight: 19023},
        {name:"Torres", weight: 4019},
        {name:"Cech", weight: 9626},
    ]
    
    var i;

    var weights = [];

    for (i = 0; i < options.length; i++)
        weights[i] = options[i].weight + (weights[i - 1] || 0);
    
    var random = Math.random() * weights[weights.length - 1];
    
    for (i = 0; i < weights.length; i++)
        if (weights[i] > random)
            break;
    

  var sourceOfPicture = "icons/"+(options[i].name).toUpperCase()+".png";
  var img = document.getElementById('bigpic')
  img.src = sourceOfPicture;
  img.style.display = "block";

}

