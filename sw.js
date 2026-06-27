// ================================================================
// Service Worker – Dillimore Projects
// ================================================================

const CACHE_NAME = 'dillimore-v1';
const urlsToCache = [
  '/',
  '/StarWars.html',
  '/Snake.html',
  '/Calculator.html',
  '/Calendar.html',
  '/404.html',
  'https://uploadkon.ir/uploads/0bd526_26InShot-20250821-043319341.png'
];

// Install Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Activate Service Worker
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Fetch from cache or network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
