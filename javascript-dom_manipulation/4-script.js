document.querySelector('#add_item').addEventListener('click', function () {
  document.createElement('li').textContent = 'Item';
  document.querySelector('.my_list').appendChild(document.createElement('li'));
});
