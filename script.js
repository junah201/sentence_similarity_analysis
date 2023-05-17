function calculateResult() {
	const sentence1 = document.getElementById("sentence1").value;
	const sentence2 = document.getElementById("sentence2").value;
	var resultElement = document.getElementById("result");
	resultElement.innerText = "Loading...";

	axios({
		url: "https://jsigrjyt1a.execute-api.ap-northeast-2.amazonaws.com/prod",
		method: "POST",
		data: {
			sentence1: sentence1,
			sentence2: sentence2,
		},
		headers: {
			"Content-Type": "application/json",
		},
	})
		.then((response) => {
			console.log(response.data);
			resultElement.innerText = `문장1 : ${response.data.morphs1.join(
				" | "
			)}\n문장2 : ${response.data.morphs2.join(" | ")}\n\n코사인 유사도: ${
				response.data.cosine_similarity
			}\n자카드 유사도: ${response.data.jaccard_similarity}\n유클리디안 거리: ${
				response.data.euclidean_distance
			}`;
		})
		.catch((error) => {
			console.log(error);
		});
}
