// import { Component, Input, OnInit } from '@angular/core';
// import { VacancyService } from '../../services/vacancy.service';
// import { Vacancy } from '../../models/vacancy';
// import { CommonModule } from '@angular/common'; // нужно для *ngFor
// import { HttpClientModule } from '@angular/common/http'; // нужно, если service использует http

// @Component({
//   selector: 'app-vacancy-list',
//   standalone: true, // 👈 вот это добавляем!
//   imports: [CommonModule], // 👈 обязательно
//   templateUrl: './vacancy-list.component.html',
//   styleUrls: ['./vacancy-list.component.css']
// })
// export class VacancyListComponent implements OnInit {
//   @Input() companyId: number | null = null;
//   vacancies: Vacancy[] = [];

//   constructor(private vacancyService: VacancyService) {}

//   ngOnInit(): void {
//     if (this.companyId) {
//       this.vacancyService.getVacanciesByCompany(this.companyId).subscribe((data) => {
//         this.vacancies = data;
//       });
//     }
//   }
// }
import { Component, Input } from '@angular/core';
import { Vacancy } from '../../models/vacancy';
import { CommonModule } from '@angular/common';
@Component({
  standalone: true, // если ты используешь standalone
  imports: [CommonModule],
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
})
export class VacancyListComponent {
  @Input() vacancies: Vacancy[] = [];
}

