# Trendagram

This is the code of an [AWS Lambda function][0] and this basically sends [Twitter trends][1] to me via [Telegram][2] on an hourly basis.

## How the deployment works

1. Once code is pushed to the `main` branch, the code gets built using a Github webhook trigger in [AWS Codebuild][3].
2. AWS Codebuild builds the code and places the built [Docker image][4] into [AWS Elastic Container Registry][5] (ECR).
3. Apart from placing the built image, it also sends out a message on an [AWS SNS topic][6] signifying that code was built successfully.
4. Another Lambda function is subscribed to this SNS topic, and upon reception of the completion message from Codebuild, it uses the [update_function_code][7] call in the AWS Python SDK ([boto3][8]) to update and publish the ECR image as a new version of the Trendagram function.
5. Once this is successful, the deployer (secondary) lambda sends out an email of successful deployment through another SNS topic.
6. [AWS CloudWatch][9] is used to log everything across the entire deployment.

## How the code works

This lambda container is set to run as per a scheduled [cron job][10] via an [AWS EventBridge][11] trigger.

During execution, it fetches the Twitter trends for a location using the [tweepy][12] module, and uses the [sendMessage][13] method of Telegram Bot API to send the trends using the [TrendagramBot][14]. I've tried to make all the variables as environment variables for easy portability.

## Future plans

Currently, the code sends trends of a particular location using its [WOEID][15]. It'd be great if it can fetch and send personalised trends instead of location-wise trends.

<!-- LINKS -->
[0]: https://aws.amazon.com/lambda/
[1]: https://twitter.com/explore/tabs/trending
[2]: https://telegram.org
[3]: https://aws.amazon.com/codebuild/
[4]: https://www.docker.com
[5]: https://aws.amazon.com/ecr/
[6]: https://aws.amazon.com/sns
[7]: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_function_code
[8]: https://aws.amazon.com/sdk-for-python/
[9]: https://aws.amazon.com/cloudwatch/
[10]: https://en.wikipedia.org/wiki/Cron
[11]: https://aws.amazon.com/eventbridge/
[12]: https://www.tweepy.org
[13]: https://core.telegram.org/bots/api#sendmessage
[14]: https://t.me/trendagram_bot
[15]: https://en.wikipedia.org/wiki/WOEID
