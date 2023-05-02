import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsListComponent } from './components/products-list/products-list.component';
//import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

///angular
import { FormsModule } from "@angular/forms";
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";

//import { AuthGuard } from './guard/auth.guard';
//import { TokenInterService } from './services/token-inter.service';
//import { CarritocomprasComponent } from './components/carritocompras/carritocompras.component';

/*Angular Materia*/
import {MatTableModule} from '@angular/material/table';
import {MatCardModule} from '@angular/material/card';
import {MatDialogModule} from '@angular/material/dialog';
import {MatSortModule} from '@angular/material/sort';
import {BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatPaginatorModule} from '@angular/material/paginator';

@NgModule({
  declarations: [
    AppComponent,
    ProductsListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,

    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,

    MatTableModule,
    MatCardModule,
    MatDialogModule,
    MatSortModule,
    MatPaginatorModule
  ],
  providers: [
    /*AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterService,
      multi: true
    }*/
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
