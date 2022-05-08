# 📌 My Ninth Project 📋

---

##### - Outline : 2022년 4월 22일, 아홉번째 관통 프로젝트를 수행하였다. 이제 정말 얼마 남지 않았다고 생각이 든다. 다음주에 마지막 관통프로젝트를 수행하면, 최종프로젝트만 앞두고 있게 될 것이다. 그러면서 오늘 느꼈던 점에 대해 간단하게 여기에 적어보도록 하겠다.

#####  오늘 프로젝트는 조금 특이하다고 느껴졌던 점이 있었다. 어느 정도 자율성이 보장되어 있다는 것이다. 그 말은 곧 기능 면에 있어서는 작동이 될 수 있게끔 작성하되, 그 외는 모든 것이 팀 별로 자유롭게 구성하라는 뜻이었다. 예를 들자면, 적절한 알고리즘을 사용하여 영화를 추천할 수 있게 한다는 것이 그러하였다. 그렇기에 더 팀원과 이야기를 나눌 수 있게 된 것 같고, 서로 생각을 나눌 수 있다는 것이 곧 개발이지 않을까 생각을 했던 날이기도 하였다.

#####  오늘 프로젝트를 하면서 느낀 점부터 한 줄로 간단하게 말하자면, '주말동안 많은 복습을 통해 더 많은 도움이 되어주고 싶다.' 였다. 오늘은 같은 반의 '고은민' 학우와 페어를 이루어 프로젝트를 수행하였고, 그 과정 속에서 느낀 점을 중심으로 서술해 보고자 한다. 또한 개선해야 하는 부분도 작성해보려 한다.

---

<br>


# **< Title : "알고리즘을 적용한 서버 구성" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *요구사항 : 커뮤니티 서비스의 상세 기능 개발을 위한 단계로, 비동기 통신(AJAX)을 활용하여 사용자의 UI/UX를 개선할 수 있습니다.*

---

*(프로젝트 파일의 settings.py, urls.py와 base.html 등의 기본 설정은 제외하고 , 앱 파일에 관해서만 작성합니다.)*

<br>

- **유저 팔로우 기능 구현**

  - **accounts/views.py**

    ```python
    # follow 기능에 대해서만 작성.
    
    @require_POST
    def follow(request, user_pk):
        followed = False
        if request.user.is_authenticated:
            person = get_object_or_404(get_user_model(), pk=user_pk)
            user = request.user
            if person != user:
                if person.followers.filter(pk=user.pk).exists():
                    person.followers.remove(user)
                else:
                    person.followers.add(user)
                    followed = True
            context = {
                'followed': followed,
                'followerCount': user.followers.count(),
                'followingCount': user.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:login')
    ```

  - **accounts/profile.html**

    ```python
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>{{ person.username }}의 프로필 페이지</h1>
      {% with followings=person.followings.all followers=person.followers.all %}
        <div>
          <div id='follow-count'>
            팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
          </div>
          {% if request.user != person %}
            <div>
              <form action="{% url 'accounts:follow' person.pk %}" id="follow-form" method="POST" data-user-id="{{ person.pk }}">
                {% if request.user.is_authenticated %}
                  {% csrf_token %}
                {% endif %}
                {% if request.user in followers %}
                  <button id="followBtn">언팔로우</button>
                {% else %}
                  <button id="followBtn">팔로우</button>
                {% endif %}
              </form>
            </div>
          {% endif %}
        </div>
      {% endwith %}
    {% endblock %}
    
    {% block script %}
    <script>
      const followForm = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')
    
      if (followForm) {
        followForm.addEventListener('submit', event => {
          if (csrf_token) {
            event.preventDefault()
            const userId = event.target.dataset.userId
            axios({
              method: 'post',
              url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
              headers : {'X-CSRFToken': csrftoken.value},
            })
            .then(response => {
              const input = document.querySelector('#followBtn')
              if (response.data.followed) {
                input.innerText = '언팔로우'
              } else {
                input.innerText = '팔로우'
              }
              
              const followCount = document.querySelector('#follow-count')
              followCount.innerText = `팔로잉 : ${response.data.followingCount} / 팔로워 : ${response.data.followerCount}`
            })
          }
        })
      }
    </script>
    {% endblock script %}
    ```

<br>

- **리뷰 좋아요 기능 구현**

  - **community/views.py**

    ```python
    # like 기능에 대해서만 작성.
    
    @require_POST
    def like(request, review_pk):
        if request.user.is_authenticated:
            review = get_object_or_404(Review, pk=review_pk)
            user = request.user
            if review.like_users.filter(pk=user.pk).exists():
                review.like_users.remove(user)
                liked = False
            else:
                review.like_users.add(user)
                liked = True
            context = {
                'liked': liked,
                'count': review.like_users.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:login')
    ```

  - **community/index.html**

    ```python
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Community</h1>
      <hr>
      {% for review in reviews %}
        <p>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></p>
        <p>글 번호: {{ review.pk }}</p>
        <p>글 제목: {{ review.title }}</p>
        <p>글 내용: {{ review.content }}</p>
        <form action="{% url 'community:like' review.pk %}" method="POST" class="d-inline like-form" data-review-id="{{ review.pk }}">
          {% csrf_token %}
          {% if user in review.like_users.all %}
            <button id="like-{{ review.pk }}">좋아요 취소</button>
          {% else %}
            <button id="like-{{ review.pk }}">좋아요</button>
          {% endif %}
        </form>
        <p>
          <span id="like-count-{{ review.pk }}">
            {{ review.like_users.all|length }}
          </span>
          명이 이 글을 좋아합니다.
        </p>
        <a href="{% url 'community:detail' review.pk %}">[detail]</a>
        <hr>
      {% endfor %}
    {% endblock %}
    
    
    {% block script %}
    <script>
      const likeForms = document.querySelector('.like-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')
      likeForms.forEach(form => {
        forms.addEventListener('submit', event => {
          event.preventDefault()
          const reviewId = event.target.dataset.reviewId
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/community/${reviewId}/like/`,
            headers : {'X-CSRFToken': csrftoken.value},
          })
          .then(response => {
            const likeCount = document.querySelector(`#like-count-${reviewId}`)
            likeCount.innerText = response.data.count
            const button = document.querySelector(`#like-${reviewId}`)
            if (response.data.liked) {
              button.innerText = '좋아요 취소'
            } else {
              button.innerText = '좋아요'
            }
          })
        })
      })
    </script>
    {% endblock script %}
    ```

<br>

- **사용자의 인증 여부와 관계없이, 전체 영화 목록 조회 페이지에서 영화 목록을 제공하는 기능 구현**

  - **movies/views.py**

    ```python
    # 목적에 맞는 코드만 작성.
    
    @require_safe
    def index(request):
        movies = Movie.objects.order_by('-popularity')
        paginator = Paginator(movies, 10)
        page_number = request.GET.get('page')
        # queryset
        page_obj = paginator.get_page(page_number)
        
        context = {
            'movies': page_obj,
        }
        return render(request, 'movies/index.html', context)
    ```

  - **movies/index.html**

    ```python
    {% extends 'base.html' %}
    {% load bootstrap5 %}
    {% block content %}
      <h1>Movies</h1>
    
      <div id="movieList">
        {% for movie in movies %}
        <div class="movie">
          <h2>{{ movie.title }}</h2>
          <p>{{ movie.overview }}</p>
          <a href="{% url 'movies:detail' movie.pk %}">[DETAIL]</a>
          <hr>
        </div>
        {% endfor %}
    
        <!-- 여기에 JSON 내용을 담은 Element append -->
      </div>
    
    {% comment %} 
      <div class="d-flex justify-content-center">
        {% bootstrap_pagination movies %}
      </div> {% endcomment %}
    {% endblock %}
    
    {% block script %}
    <script>
      let page = 2
      const movieList = document.querySelector('#movieList')
    
      document.addEventListener('scroll', function (event) {
        const { scrollTop, clientHeight, scrollHeight } = document.documentElement
        // 완전 바닥에 도달
        // if (scrollHeight - scrollTop === clientHeight) {
    
        // 1. 스크롤이 바닥(언저리)에 도달 했을때, => document / event 
        if (scrollTop + clientHeight >= scrollHeight - 5) {
          // 2. 추가 데이터 10개를 불러옴(AJAX) => axios / DRF
          axios({
            method: 'get',
            url: `/movies/ajax/?page=${page}`
          })
            .then(res => {
                const movies = res.data
                // 3. 응답 JSON 데이터 10개를 화면에 붙임
                movies.forEach(movie => {
                  const movieDiv = document.createElement('div')
    
                  const h2 = document.createElement('h2')
                  h2.innerText = movie.title
    
                  const p = document.createElement('p')
                  p.innerText = movie.overview
    
                  const a = document.createElement('a')
                  a.innerText = '[DETAIL]'
                  a.href = `/movies/${movie.id}/`
    
                  const hr = document.createElement('hr')
    
                  movieDiv.append(h2, p, a, hr)
                  movieList.appendChild(movieDiv)
                })
                page++
              })
              .catch(err => console.error(err))
        }
      })
    </script>
    {% endblock script %}
    ```
    
  

<br>

- **사용자의 인증 여부와 관계없이, 단일 영화 상세 조회 페이지에서 영화 정보를 제공하는 기능 구현**

  - **movies/views.py**

    ```python
    # 목적에 맞는 코드만 작성.
    
    @require_safe
    def detail(request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        context = {
            'movie': movie,
        }
        return render(request, 'movies/detail.html', context)
    ```

  - **movies/detail.html**

    ```python
    {% extends 'base.html' %}
    
    {% block content %}
      <h2 class="text-center">DETAIL</h2>
      <h3>{{ movie.pk }} 번째 글</h3>
      <hr>
      <p>title: {{ movie.title }}</p>
      <p>release_date: {{ movie.release_date }}</p>
      <p>popularity: {{ movie.popularity }}</p>
      <p>vote_count: {{ movie.vote_count }}</p>
      <p>vote_average: {{ movie.vote_average }}</p>
      <p>overview: {{ movie.overview }}</p>
      <p>
        <img src="{{ movie.poster_path }}" alt="">
      </p>
      <hr>
      <a href="{% url 'movies:index' %}">[back]</a>
    {% endblock  %}
    ```

<br>

- **사용자가 인증되어 있다면, 10개의 영화를 추천하여 제공할 수 있는 기능 구현**

  - **movies/views.py**

    ```python
    @require_safe
    def recommended(request):
        if request.user.is_authenticated:
            movies = Movie.objects.order_by('-vote_average')[:10]
            context = {
                'movies': movies,
            }
            return render(request, 'movies/recommended.html', context)
        return redirect('accounts:login')
    ```

  - **movies/recommended.html**

    ```python
    {% extends 'base.html' %}
    
    {% block content %}
      <h2 class="text-center">영화 추천</h2>
      {% for movie in movies  %}
        <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
        <hr>
      {% endfor %}
    {% endblock %}
    ```

<br>

---







