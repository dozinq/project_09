# ๐ My Ninth Project ๐

---

##### - Outline : 2022๋ 5์ 6์ผ, ์ํ๋ฒ์งธ ๊ดํต ํ๋ก์ ํธ๋ฅผ ์ํํ์๋ค. ์ด์  ์ ๋ง ์ผ๋ง ๋จ์ง ์์๋ค๊ณ  ์๊ฐ์ด ๋ ๋ค. ๋ค์์ฃผ์ ๋ง์ง๋ง ๊ดํตํ๋ก์ ํธ๋ฅผ ์ํํ๋ฉด, ์ต์ขํ๋ก์ ํธ๋ง ์๋๊ณ  ์๊ฒ ๋  ๊ฒ์ด๋ค. ๊ทธ๋ฌ๋ฉด์ ์ค๋ ๋๊ผ๋ ์ ์ ๋ํด ๊ฐ๋จํ๊ฒ ์ฌ๊ธฐ์ ์ ์ด๋ณด๋๋ก ํ๊ฒ ๋ค.

#####  ์ค๋ ํ๋ก์ ํธ๋ ์กฐ๊ธ ํน์ดํ๋ค๊ณ  ๋๊ปด์ก๋ ์ ์ด ์์๋ค. ์ด๋ ์ ๋ ์์จ์ฑ์ด ๋ณด์ฅ๋์ด ์๋ค๋ ๊ฒ์ด๋ค. ๊ทธ ๋ง์ ๊ณง ๊ธฐ๋ฅ ๋ฉด์ ์์ด์๋ ์๋์ด ๋  ์ ์๊ฒ๋ ์์ฑํ๋, ๊ทธ ์ธ๋ ๋ชจ๋  ๊ฒ์ด ํ ๋ณ๋ก ์์ ๋กญ๊ฒ ๊ตฌ์ฑํ๋ผ๋ ๋ป์ด์๋ค. ์๋ฅผ ๋ค์๋ฉด, ์ ์ ํ ์๊ณ ๋ฆฌ์ฆ์ ์ฌ์ฉํ์ฌ ์ํ๋ฅผ ์ถ์ฒํ  ์ ์๊ฒ ํ๋ค๋ ๊ฒ์ด ๊ทธ๋ฌํ์๋ค. ๊ทธ๋ ๊ธฐ์ ๋ ํ์๊ณผ ์ด์ผ๊ธฐ๋ฅผ ๋๋ ์ ์๊ฒ ๋ ๊ฒ ๊ฐ๊ณ , ์๋ก ์๊ฐ์ ๋๋ ์ ์๋ค๋ ๊ฒ์ด ๊ณง ๊ฐ๋ฐ์ด์ง ์์๊น ์๊ฐ์ ํ๋ ๋ ์ด๊ธฐ๋ ํ์๋ค.

#####  ์ค๋ ํ๋ก์ ํธ๋ฅผ ํ๋ฉด์ ๋๋ ์ ๋ถํฐ ํ ์ค๋ก ๊ฐ๋จํ๊ฒ ๋งํ์๋ฉด, '์ฃผ๋ง๋์ ๋ง์ ๋ณต์ต์ ํตํด ๋ ๋ง์ ๋์์ด ๋์ด์ฃผ๊ณ  ์ถ๋ค.' ์๋ค. ์ค๋์ ๊ฐ์ ๋ฐ์ '๊ณ ์๋ฏผ' ํ์ฐ์ ํ์ด๋ฅผ ์ด๋ฃจ์ด ํ๋ก์ ํธ๋ฅผ ์ํํ์๊ณ , ๊ทธ ๊ณผ์  ์์์ ๋๋ ์ ์ ์ค์ฌ์ผ๋ก ์์ ํด ๋ณด๊ณ ์ ํ๋ค. ๋ํ ๊ฐ์ ํด์ผ ํ๋ ๋ถ๋ถ๋ ์์ฑํด๋ณด๋ ค ํ๋ค.

---

<br>


# **< Title : "์๊ณ ๋ฆฌ์ฆ์ ์ ์ฉํ ์๋ฒ ๊ตฌ์ฑ" >**

*(This project was carried out in **Python 3.9.9 and Django 3.2.12 environment .**)*

- *์๊ตฌ์ฌํญ : ์ปค๋ฎค๋ํฐ ์๋น์ค์ ์์ธ ๊ธฐ๋ฅ ๊ฐ๋ฐ์ ์ํ ๋จ๊ณ๋ก, ๋น๋๊ธฐ ํต์ (AJAX)์ ํ์ฉํ์ฌ ์ฌ์ฉ์์ UI/UX๋ฅผ ๊ฐ์ ํ  ์ ์์ต๋๋ค.*

---

*(ํ๋ก์ ํธ ํ์ผ์ settings.py, urls.py์ base.html ๋ฑ์ ๊ธฐ๋ณธ ์ค์ ์ ์ ์ธํ๊ณ  , ์ฑ ํ์ผ์ ๊ดํด์๋ง ์์ฑํฉ๋๋ค.)*

<br>

- **์ ์  ํ๋ก์ฐ ๊ธฐ๋ฅ ๊ตฌํ**

  - **accounts/views.py**

    ```python
    # follow ๊ธฐ๋ฅ์ ๋ํด์๋ง ์์ฑ.
    
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
      <h1>{{ person.username }}์ ํ๋กํ ํ์ด์ง</h1>
      {% with followings=person.followings.all followers=person.followers.all %}
        <div>
          <div id='follow-count'>
            ํ๋ก์ : {{ followings|length }} / ํ๋ก์ : {{ followers|length }}
          </div>
          {% if request.user != person %}
            <div>
              <form action="{% url 'accounts:follow' person.pk %}" id="follow-form" method="POST" data-user-id="{{ person.pk }}">
                {% if request.user.is_authenticated %}
                  {% csrf_token %}
                {% endif %}
                {% if request.user in followers %}
                  <button id="followBtn">์ธํ๋ก์ฐ</button>
                {% else %}
                  <button id="followBtn">ํ๋ก์ฐ</button>
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
                input.innerText = '์ธํ๋ก์ฐ'
              } else {
                input.innerText = 'ํ๋ก์ฐ'
              }
              
              const followCount = document.querySelector('#follow-count')
              followCount.innerText = `ํ๋ก์ : ${response.data.followingCount} / ํ๋ก์ : ${response.data.followerCount}`
            })
          }
        })
      }
    </script>
    {% endblock script %}
    ```

<br>

- **๋ฆฌ๋ทฐ ์ข์์ ๊ธฐ๋ฅ ๊ตฌํ**

  - **community/views.py**

    ```python
    # like ๊ธฐ๋ฅ์ ๋ํด์๋ง ์์ฑ.
    
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
        <p>์์ฑ์ : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></p>
        <p>๊ธ ๋ฒํธ: {{ review.pk }}</p>
        <p>๊ธ ์ ๋ชฉ: {{ review.title }}</p>
        <p>๊ธ ๋ด์ฉ: {{ review.content }}</p>
        <form action="{% url 'community:like' review.pk %}" method="POST" class="d-inline like-form" data-review-id="{{ review.pk }}">
          {% csrf_token %}
          {% if user in review.like_users.all %}
            <button id="like-{{ review.pk }}">์ข์์ ์ทจ์</button>
          {% else %}
            <button id="like-{{ review.pk }}">์ข์์</button>
          {% endif %}
        </form>
        <p>
          <span id="like-count-{{ review.pk }}">
            {{ review.like_users.all|length }}
          </span>
          ๋ช์ด ์ด ๊ธ์ ์ข์ํฉ๋๋ค.
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
              button.innerText = '์ข์์ ์ทจ์'
            } else {
              button.innerText = '์ข์์'
            }
          })
        })
      })
    </script>
    {% endblock script %}
    ```

<br>

- **์ฌ์ฉ์์ ์ธ์ฆ ์ฌ๋ถ์ ๊ด๊ณ์์ด, ์ ์ฒด ์ํ ๋ชฉ๋ก ์กฐํ ํ์ด์ง์์ ์ํ ๋ชฉ๋ก์ ์ ๊ณตํ๋ ๊ธฐ๋ฅ ๊ตฌํ**

  - **movies/views.py**

    ```python
    # ๋ชฉ์ ์ ๋ง๋ ์ฝ๋๋ง ์์ฑ.
    
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
    
        <!-- ์ฌ๊ธฐ์ JSON ๋ด์ฉ์ ๋ด์ Element append -->
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
        // ์์  ๋ฐ๋ฅ์ ๋๋ฌ
        // if (scrollHeight - scrollTop === clientHeight) {
    
        // 1. ์คํฌ๋กค์ด ๋ฐ๋ฅ(์ธ์ ๋ฆฌ)์ ๋๋ฌ ํ์๋, => document / event 
        if (scrollTop + clientHeight >= scrollHeight - 5) {
          // 2. ์ถ๊ฐ ๋ฐ์ดํฐ 10๊ฐ๋ฅผ ๋ถ๋ฌ์ด(AJAX) => axios / DRF
          axios({
            method: 'get',
            url: `/movies/ajax/?page=${page}`
          })
            .then(res => {
                const movies = res.data
                // 3. ์๋ต JSON ๋ฐ์ดํฐ 10๊ฐ๋ฅผ ํ๋ฉด์ ๋ถ์
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

- **์ฌ์ฉ์์ ์ธ์ฆ ์ฌ๋ถ์ ๊ด๊ณ์์ด, ๋จ์ผ ์ํ ์์ธ ์กฐํ ํ์ด์ง์์ ์ํ ์ ๋ณด๋ฅผ ์ ๊ณตํ๋ ๊ธฐ๋ฅ ๊ตฌํ**

  - **movies/views.py**

    ```python
    # ๋ชฉ์ ์ ๋ง๋ ์ฝ๋๋ง ์์ฑ.
    
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
      <h3>{{ movie.pk }} ๋ฒ์งธ ๊ธ</h3>
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

- **์ฌ์ฉ์๊ฐ ์ธ์ฆ๋์ด ์๋ค๋ฉด, 10๊ฐ์ ์ํ๋ฅผ ์ถ์ฒํ์ฌ ์ ๊ณตํ  ์ ์๋ ๊ธฐ๋ฅ ๊ตฌํ**

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
      <h2 class="text-center">์ํ ์ถ์ฒ</h2>
      {% for movie in movies  %}
        <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
        <hr>
      {% endfor %}
    {% endblock %}
    ```

<br>

---







