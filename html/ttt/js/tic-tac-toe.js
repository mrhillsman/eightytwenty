let current_player, symbol, game_over, winner, tie, move_count, game_started

function reset_gameboard() {
    let columns = document.getElementById('gameboard').children;
    for (let squares of columns) {
        for (let square of squares.children) {
            square.innerHTML = "";
        }
    }
}

function initiate_game() {
    current_player = "";
    symbol = "";
    game_over = false;
    winner = "";
    tie = false;
    move_count = 0;
    game_started = false;

    reset_gameboard();

    Math.random() < 0.5 ? symbol = "X" : symbol = "O";
    if (symbol === "X") {
        current_player = "x-player";
    } else {
        current_player = "o-player";
    }

    let players = document.getElementById('players').children;
    for (let player of players) {
        if (player.id === current_player) {
            player.setAttribute('class', 'border-b-2 border-black active');
        } else {
            player.setAttribute('class', '')
        }
    }
}

function switch_player() {
    document.getElementById(current_player).setAttribute('class', '');

    if (current_player === "x-player") {
        current_player = "o-player";
        symbol = "O";
    } else {
        current_player = "x-player";
        symbol = "X";
    }

    document.getElementById(current_player).setAttribute('class', 'border-b-2 border-black active');
}

function place_symbol(square) {
    document.getElementById(square).innerHTML = symbol;
}

function start_game() {
    initiate_game();
    game_started = true;
    document.getElementById('game-status').innerHTML = "Game Started";
    document.getElementById('reset-game').removeAttribute('disabled');
    document.getElementById('reset-game').addEventListener('click', reset_game);
}

function reset_game() {
    initiate_game();
    for (let player of document.getElementById('players').children) {
        player.setAttribute('class', '');
    }
    document.getElementById('game-status').innerHTML = "Press Start Game Again";
}

function update_gameboard(e) {
    if (!game_started || game_over) {
        return;
    }

    if (document.getElementById(e.target.id).innerHTML === '') {
        place_symbol(e.target.id);
        switch_player();
        move_count++;
        if (move_count === 9) {
            game_over = true;
            tie = true;
            return;
        }

        check_for_winner();
    }
}

function check_for_winner() {
    function check_rows() {

    }
    function check_columns() {

    }

    function check_diagonals() {

    }
}

document.getElementById('gameboard').addEventListener('click', update_gameboard);

document.getElementById('start-game').addEventListener('click', start_game);