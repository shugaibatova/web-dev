import { NgModule } from '@angular/core';  // ❗ Добавьте эту строку
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    HttpClientModule
  ]
})
export class AppModule { }