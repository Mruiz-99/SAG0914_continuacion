import { Component, OnInit } from '@angular/core';

import {AfterViewInit, ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';

import { ServiciosService } from '../../services/servicios.service';
import { MatTableDataSource } from '@angular/material/table';
//import {DataSharingService} from "../../data-sharing.service";

import {BehaviorSubject} from "rxjs";

import {AppComponent} from "../../app.component";


@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css']
})
export class ProductsListComponent implements OnInit {

  displayedColumns: string[] = ['sku','actionsboton', 'info', 'nombre', 'categoria', 'stock'];
  dataSource = new MatTableDataSource();

  @ViewChild(MatPaginator)
  paginator!: MatPaginator;


  categorias: any = [];
  idCategoria:number = 99;
  constructor(public productService: ServiciosService, /*private dataSharingService: DataSharingService,*/ private carit:AppComponent) { }

  products: any = [];

  ngOnInit(): void {
    this.getProductos()
  }

  getProductos() {
    this.productService.getProductos()
      .subscribe(
        (res: any) => {
          
          console.log(res.productos)
          this.products = res.productos;
          this.dataSource.data = this.products;
          this.dataSource.paginator = this.paginator;
        },
        err => console.error(err.error)
      );
  }

}
