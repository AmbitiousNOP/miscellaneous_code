// setup canvas
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const width = (canvas.width = window.innerWidth);
const height = (canvas.height = window.innerHeight);

// function to generate random number
function random(min, max) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    return num;
}

// function to generate random color
function randomRGB() {
    return `rgb(${random(0, 255)},${random(0, 255)},${random(0, 255)})`;
}

class Shape { 
    constructor(x,y,velX,velY){
        this.x = x;
        this.y = y;
        this.velX = velX;
        this.velY = velY;
    }
}

class EvilCircle extends Shape {
    constructor(x,y,velX,velY,color,size){
        super(x,y,20,20);
        this.color = "white";
        this.size = 10;

        window.addEventListener("keydown", (e) => {
            switch (e.key) {
            case "a":
                this.x -= this.velX;
                break;
            case "d":
                this.x += this.velX;
                break;
            case "w":
                this.y -= this.velY;
                break;
            case "s":
                this.y += this.velY;
                break;
            }
        });
    }

    draw() { 
        ctx.beginPath();
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 3;
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        ctx.stroke();
    }

    // copied from ball class. Not sure if it'll translate very well. 
    collisionDetect() {
        for (const ball of balls){
            if ((this !== ball) && ball.exists){
                const dx = this.x - ball.x;
                const dy = this.y - ball.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + ball.size){
                    ball.color = this.color = randomRGB();
                }
            }
        }
    }

}


class Ball extends Shape{
    constructor(x, y, velX, velY, color, size){
        super(x,y,velX,velY);
        this.color = color;
        this.size = size;
    }
    
    draw() { 
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        ctx.fill();
    }

    update() {
        if ((this.x + this.size) >= width) {
            this.velX = -(this.velX);
        }

        if ((this.x - this.size) <= 0) {
            this.velX = -(this.velX);
        }

        if ((this.y + this.size) >= height) {
            this.velY = -(this.velY);
        }

        if ((this.y - this.size) <= 0) {
            this.velY = -(this.velY);
        }

        this.x += this.velX;
        this.y += this.velY;
    }

    exists() {
        // function to determine if the ball exits. (i.e. if it's been hit by the player)
        // three methods to do this 
        // (1) check if ball is within the canvas boundaries
        // (2) check for collisions with other objects
        // (3) check if the ball is moving
        if (((this.x > 0) && (this.x < width)) && ((this.y > 0) && (this.y < height))){
            return true;
        }else{
            return false;
        }
    }

    collisionDetect() {
        for (const ball of balls){
            if ((this !== ball) && ball.exists){
                const dx = this.x - ball.x;
                const dy = this.y - ball.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + ball.size){
                    ball.color = this.color = randomRGB();
                }
            }
        }
    }
}

const balls = [];

while (balls.length < 25){
    const size = random(10,20);
    const ball = new Ball(
        random(0 + size, width-size),
        random(0 + size, height-size),
        random(-7,7),
        random(-7,7),
        randomRGB(),
        size,
    );

    balls.push(ball);
}

// define evil ball
const player_ball = new EvilCircle(
    random(0 + 10, width-10),
    random(0 + 10, height-10)   
);


function loop() {
    ctx.fillStyle = "rgba(0,0,0,0.25)";
    ctx.fillRect(0,0,width,height);

    player_ball.draw();
    for (const ball of balls){
        ball.draw();
        ball.update();
        ball.collisionDetect();
    }

    requestAnimationFrame(loop);
}

loop();

