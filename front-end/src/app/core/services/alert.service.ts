import { Injectable } from '@angular/core';

declare var swal: any;
declare var toastr: any;

@Injectable({
  providedIn: 'root'
})
export class AlertService {

  constructor() {

  }
  alert(title: string, text: string, icon: string) {
    swal.fire(
      title,
      text,
      icon
    );
  }
  notification(title: string, text: string, type: string) {
    if (title !== null) {
      toastr[type](text, title)
    } else {
      toastr[type](text)
    }
  }
}
