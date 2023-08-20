// Check if current_player is already set
// If not, set current_player to either "X" or "O" randomly
function set_current_player() {
    let current_player = "";
    Math.random() < 0.5 ? current_player = "X" : current_player = "O";
    return current_player;
}

function start_new_game() {

}

function check_for_winner_or_tie() {

    return [false, "", false];
}

function switch_players(current_player) {
    // Change current_player to X if it is O otherwise change it to O
    if (current_player === "X") {
        return "O";
    }

    return "X";
}

function place_symbol(current_player, square) {
    // Place current_player symbol in square
    document.getElementById(square).innerHTML = current_player;
}

function run() {
    let current_player = set_current_player();
    let game_over = false;
    let winner = "";
    let tie = false;

    document.getElementById('gameboard').addEventListener('click', function(e) {
        if(document.getElementById(e.target.id).innerHTML === '') {
            place_symbol(current_player, e.target.id);
            switch_players(current_player);
        }
    });

    while (!game_over) {
        [game_over, winner, tie] = check_for_winner_or_tie();
    }

    if (tie) {
        console.log("It's a tie!");
    } else {
        console.log("Player " + winner + " wins!");
    }
}

// run();