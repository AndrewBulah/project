# Drupal-like CMS на Python
```bash
┌───────────────┐       ┌──────────────┐       ┌──────────────┐
│   GitHub      │       │   Docker Hub  │       │  Kubernetes   │
│  Repository   │──────▶│    Registry   │──────▶│    Cluster    │
└───────────────┘       └──────────────┘       └──────────────┘
                                                  ▲
                                                  │
                                             ┌──────────────┐
                                             │    ArgoCD     │
                                             │  Application  │
                                             └──────────────┘
                                                  │
                                                  ▼
                                             ┌──────────────┐
                                             │  Helm Chart   │
                                             │ (drupal-app)  │
                                             └──────────────┘
                                                  │
                                                  ▼
                                             ┌──────────────┐
                                             │   MariaDB     │
                                             │ (StatefulSet) │
                                             └──────────────┘
                                          
```
