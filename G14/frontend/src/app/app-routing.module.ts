import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


import { ProductsListComponent } from "./components/products-list/products-list.component";
const routes: Routes = [
  {
    path: '',
    redirectTo: '/products',
    pathMatch: 'full'
  },
    ////lista de productos
    {
      /*protegida*/
      path: 'products',
      component: ProductsListComponent/*,
      canActivate: [AuthGuard]*/
    }, 
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
