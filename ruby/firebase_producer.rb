require 'firebase'


class FirebaseProducer
  def initialize
    @products = Array['apple', 'apricot', 'cherry', 'lemon', 'lime', 'mango', 'orange']
    @idx = 0
    base_url = 'https://proyectoorgange.firebaseio.com'
    private_key_json_string = File.open('../serviceAccountCredentials.json').read
    @firebase = Firebase::Client.new(base_url, private_key_json_string)
  end

  def make_product
    @firebase.set('products', @products[@idx])
    @idx = (1 + @idx) % @products.size
  end

  def producer_loop
    loop do
      make_product
      sleep(2)
    end
  end
end


p = FirebaseProducer.new
p.producer_loop

