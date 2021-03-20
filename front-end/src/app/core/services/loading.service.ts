import { Injectable } from '@angular/core';

declare var KTApp: any;
@Injectable({
  providedIn: 'root'
})
export class LoadingService {

  constructor() { }
  setLoading(status: boolean) {
    if (status) {
      KTApp.block(document.body, { overlayColor: '#525252', opacity: .5 });
    } else {
      KTApp.unblock(document.body);
    }
  }
}
