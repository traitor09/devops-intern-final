import mlflow


if __name__ == "__main__":
    mlflow.set_experiment("devops-demo")

    with mlflow.start_run():
        # Log dummy parameters
        mlflow.log_param("optimizer", "adam")
        mlflow.log_param("learning_rate", 0.01)

        # Log dummy metrics
        mlflow.log_metric("accuracy", 0.92)
        mlflow.log_metric("loss", 0.08)

        print("MLflow run completed")
