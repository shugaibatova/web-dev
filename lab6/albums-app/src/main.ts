// import { bootstrapApplication } from '@angular/platform-browser';
// import { appConfig } from './app/app.config';
// import { AppComponent } from './app/app.component';

// bootstrapApplication(AppComponent, appConfig)
//   .catch((err) => console.error(err));
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { importProvidersFrom } from '@angular/core';
import { FormsModule } from '@angular/forms';

// Настраиваем маршруты
import { HomeComponent } from './app/home/home.component';
import { AboutComponent } from './app/about/about.component';
import { AlbumsComponent } from './app/albums/albums.component';
import { AlbumDetailComponent } from './app/album-detail/album-detail.component';
import { AlbumPhotosComponent } from './app/album-photos/album-photos.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter([
      { path: '', redirectTo: '/home', pathMatch: 'full' },
      { path: 'home', component: HomeComponent },
      { path: 'about', component: AboutComponent },
      { path: 'albums', component: AlbumsComponent },
      { path: 'albums/:id', component: AlbumDetailComponent },
      { path: 'albums/:id/photos', component: AlbumPhotosComponent },
    ]),
    provideHttpClient(),
    importProvidersFrom(FormsModule), // Добавляем поддержку форм
  ],
}).catch(err => console.error(err));
