# Drupal-like CMS на Python
```mermaid
graph TD
    A[GitHub] --> B{CI/CD Pipeline}
    B --> C[Build Docker Image]
    C --> D[Push to Docker Hub]
    B --> E[Run Tests]
    E --> F{k6 Load Test}
    F --> G[ArgoCD Sync]
    G --> H[Kubernetes Cluster]
    H --> I[Deployment]
    I --> J[Service]
    J --> K[Ingress]
    K --> L[Пользователь]
    H --> M[SealedSecret]
    M --> N[Secret]
    N --> O[MariaDB]
    O --> P[Persistent Volume]
    G --> Q[Slack Notifications]
    
    subgraph "GitHub Actions Workflow"
        B --> C
        B --> E
        E --> F
        F --> D
        D --> G
    end
    
    subgraph "Kubernetes Infrastructure"
        H --> I
        H --> M
        I --> J
        J --> K
        M --> N
        N --> O
        O --> P
    end
    
    subgraph "Database Layer"
        O -->|TCP 3306| P
    end
    
    subgraph "Networking"
        K -->|HTTP/HTTPS| L
    end
    
    Q -->|Webhook| Slack[Slack Channel]
```
1. Цель проекта
Создать отказоустойчивое веб-приложение для управления пользователями с интеграцией в Kubernetes и автоматизированными пайплайнами CI/CD.
Основные требования :

Версионирование : Использование SemVer для Docker-образов и Helm-чартов.
База данных : MariaDB с сохранением данных между обновлениями.
CI/CD : Автоматизация сборки, тестирования и деплоя через GitHub Actions и ArgoCD.
Уведомления : Slack-оповещения при успешном/неудачном деплое.
Откат : Возможность автоматического и ручного отката через Helm и ArgoCD.

2. Архитектура проекта
Компоненты :

Frontend : Веб-интерфейс на Flask (Python) с Bootstrap для стилизации.
Backend : MariaDB для хранения пользователей (таблица users).
Инфраструктура :
Kubernetes-кластер на 3 нодах (node1 — control-plane, node2 — БД, node3 — worker).
Service : LoadBalancer (MetalLB) для доступа к приложению.
Ingress : Nginx Ingress Controller для маршрутизации по домену drupal.local.
Persistent Storage : NFS-сервер на node2 для сохранения данных БД.

3. Реализация приложения
Код :

Flask-приложение (app.py):
Роуты: / (список пользователей), /add (форма добавления), /version (проверка версии).
Подключение к БД : Используются переменные окружения (например, DB_HOST, DB_USER), которые передаются через Kubernetes Secrets.

4. CI/CD-пайплайны
GitHub Actions :

Триггеры : Запуск при каждом git push в main.

5. Безопасность и надежность
SealedSecrets :
Зашифрованные данные БД хранятся в Git.
Расшифровка происходит только в кластере через контроллер.
Откат :
Helm : helm rollback drupal-app 3 (откат на ревизию 3).
ArgoCD : Автоматический откат при ошибке в образе.
Мониторинг :
Prometheus/Grafana : Отслеживание метрик приложения и БД.

6. Итог
Достижения :

Приложение доступно по http://drupal.local.
Данные сохраняются в MariaDB между обновлениями.
Автоматизация :
Сборка Docker-образов → тестирование → деплой в Kubernetes.
Откат при ошибках через ArgoCD и Helm.
Безопасность :
Нет хардкода паролей в коде.
Шифрование секретов через SealedSecrets.
Дальнейшие улучшения :

Миграции БД через Helm hooks.
Мониторинг Prometheus/Grafana.
Blue/Green деплой.
