import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";

import { map } from "rxjs/operators";
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ServiciosService {

  public URL_inven = 'http://localhost:4050';
  constructor(private http: HttpClient, private router: Router) { }

  headers: HttpHeaders = new HttpHeaders({
    "Content-Type": "application/json"
  })

  getProductos() {
    const url = this.URL_inven + '/inventario/getproductos';
    return this.http.get(url);
  }
  
}
