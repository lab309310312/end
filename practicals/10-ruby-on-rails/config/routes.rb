Rails.application.routes.draw do
  root "tasks#index"
  resources :tasks, only: %i[index create destroy] do
    patch :toggle, on: :member
  end
end
