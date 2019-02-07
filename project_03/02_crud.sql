-- 영화 극한직업 추가
INSERT INTO movies VALUES (20182530,"극한직업","15세이상관람가","이병헌",20190123,313467,111,"한국","코미디");

-- 과거의 데이터 삭제
SELECT * FROM movies WHERE "영화코드"=20040521;
DELETE FROM movies WHERE "영화코드"=20040521;

-- 영화코드 20185124 데이터 출력 & 감독="없음"으로 변경 & 확인
SELECT * FROM movies WHERE "영화코드"=20185124;
UPDATE movies SET "감독"="없음" WHERE "영화코드"=20185124;
SELECT * FROM movies WHERE "영화코드"=20185124;