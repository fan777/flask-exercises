$(function () {
  const words = new Set();
  let score = 0;
  $('#score').text(score);
  countDown();

  $('#add-word').on('submit', async function (e) {
    e.preventDefault();

    let word = $('#word').val();
    //console.log(word);

    if (!word)
      return;
    if (words.has(word)) {
      $('#msg').text(`'${word}' already played!`);
      return;
    }


    try {
      const response = await axios.get('/check-word', { params: { word: word } });
      if (response.data.result === 'not-word') {
        $('#msg').text(`'${word}' is not a word!`);
      } else if (response.data.result === 'not-on-board') {
        $('#msg').text(`'${word}' is not on board!`);
      } else {
        //$('#msg').text(`'${word}' is a word and on the board!`);
        $('#words').append($('<li>', { text: word }));
        words.add(word);
        score += word.length;
      }
      $('#score').text(score);
      $('#word').val('');
    } catch (err) {
      console.log(err.message);
    }


  });

});

function countDown() {
  let x = 60;
  let id = setInterval(function () {
    x--;
    if (x > 0) {
      $('#timer').text(x);
    } else {
      $('#word').prop('disabled', true);
      $('button').prop('disabled', true);
      $('#timer').text('Time up!');
      clearInterval(id);
    }
  }, 1000)
}