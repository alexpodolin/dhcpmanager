'use strict'
//
var row_id_modal_delete = 0;

// Покажем окно удаления подсети
// присвоим переменной row_id_modal_delete значение row-id, т.е id записи в строке
function show_modal_delete(el) {
	document.getElementById('remove__subnet').style.display = 'block';
	row_id_modal_delete = el.getAttribute('row-id');
}

// Закроем окно удаления подсети, при нажатии на "крест" или кнопку "НЕТ"
function close_modal_delete() {
	document.getElementById('remove__subnet').style.display = 'none';
}

// Нажатие на кнопку "Да" покажет .gif файл 
// затем ч.з. ajax отправит id строки в php функцию remove_subnet
// подсеть будет удалена
function remove_row() {
	document.getElementById('remove__subnet').style.display = 'none';	
	document.getElementsByClassName('progress__spin')[0].style.display = 'block';

	console.log(row_id_modal_delete);

	//  Создаём новый объект XMLHttpRequest
	var xhr = new XMLHttpRequest();	

	// Если код ответа сервера не 200, то это ошибка
	xhr.onreadystatechange = function answerReturn() {
		if (xhr.readyState == 4) {
			if (xhr.status == 200) {
				console.log(xhr.responseText + ' : ' + xhr.status + ' : ' + xhr.statusText);
				document.getElementsByClassName('progress__spin')[0].style.display = 'none';
                } 
                else {
                	console.log("Ошибка на сервере. " + xhr.status);                
            }
        }
    }

    var data = "row_id_modal_delete=" + row_id_modal_delete;

    // Метод, которым создадим запрос, который передаст переменную 
	// row_id_modal_delete в php функцию remove_subnet
	xhr.open('POST', '../func/remove_subnet.php', true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	// Отсылаем запрос
	xhr.send(data);

	// Удалим из таблички удаленную строку
	var table = document.getElementById("subnets_content");
    table.deleteRow(row_id_modal_delete);

}


