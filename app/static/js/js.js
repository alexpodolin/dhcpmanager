'use strict'

// Закроем всплывающее окно удаления, при нажатии на "крест" или кнопку "НЕТ"
function closeModalWindow() {
    var i;
    var x = document.getElementsByClassName('show__del-window');
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
}

// Покажем всплывающее окно удаления
function showModalDelete(el) {
    var i;
    var x = document.getElementsByClassName('show__del-window');
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "block";       
    }
}

// ф-ия удаления записи из БД
// Нажатие на кнопку "Да" покажет .gif файл 
// затем ч.з. ajax отправит id строки в функцию remove_subnet
// подсеть будет удалена
//function removeRow() {
//    //  Создаём новый объект XMLHttpRequest
//    var xhr = new XMLHttpRequest();  
//  	 // Если код ответа сервера не 200, то это ошибка
//    xhr.onreadystatechange = function answerReturn() {
//        if (xhr.readyState == 4) {
//            if (xhr.status == 200) {
//  				     console.log(xhr.responseText + ' : ' + xhr.status + ' : ' + xhr.statusText);
//                document.getElementsByClassName('progress__spin')[0].style.display = 'none';
//            } 
//            else {
//                console.log("Ошибка на сервере. " + xhr.status);                
//            }
//       }
//    }
  // Метод, которым создадим запрос, который передаст переменную 
  	// row_id_modal_delete в php функцию remove_subnet
//  	xhr.open('POST', '../func/remove_subnet.php', true);
//  	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  	// Отсылаем запрос
//  	xhr.send(data);
  	// Удалим из таблички удаленную строку
//  	var table = document.getElementById("subnets_content");
//  table.deleteRow(row_id_modal_delete);
//  }