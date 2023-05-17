import json
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

okt = Okt()


def jaccard_similarity(list1, list2):
    intersection = len(set(list1).intersection(set(list2)))
    union = len(set(list1)) + len(set(list2)) - intersection
    return float(intersection) / union


def calculate_cosine_similarity(morphs1, morphs2):
    # TF-IDF 벡터화 및 코사인 유사도 계산
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(
        [' '.join(morphs1), ' '.join(morphs2)])
    cosine_similarity_value = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:2])

    return cosine_similarity_value.tolist()


def lambda_handler(event, context):
    # CORS 헤더 설정
    headers = {
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS, POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Credentials': 'true',
    }

    try:
        body = event['body']
        body = json.loads(body)

        sentence1 = body['sentence1']
        sentence2 = body['sentence2']

        print(sentence1)
        print(sentence2)

        # 형태소 분석
        morphs1 = okt.morphs(sentence1)
        morphs2 = okt.morphs(sentence2)

        # 코사인 유사도 계산 함수 호출
        cosine_similarity_value = calculate_cosine_similarity(
            morphs1, morphs2)

        # Euclidean distance
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(
            [' '.join(morphs1), ' '.join(morphs2)])
        euclidean_distance_value = euclidean_distances(
            tfidf_matrix[0:1], tfidf_matrix[1:2])

        # Jaccard similarity
        jaccard_similarity_value = jaccard_similarity(morphs1, morphs2)

        # 결과 반환
        response = {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'morphs1': morphs1,
                'morphs2': morphs2,
                'cosine_similarity': cosine_similarity_value,
                'euclidean_distance': euclidean_distance_value.tolist(),
                'jaccard_similarity': jaccard_similarity_value,
            }),
        }

    except Exception as e:
        print(str(e))
        # 에러 발생 시 에러 메시지 반환
        response = {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)}),
        }

    return response
