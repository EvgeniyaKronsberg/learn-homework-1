"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    sum_of_each = 0
    total_sum = 0
    count = 0
    count_product = 0
    res_dict = {}

    # print(phones)
    print(phones[0])

    # for phone in phones:
    #     for item in phone['items_sold']:
    #         total_sum += item
    #         count += 1
    #         # print(f'Суммарное количество продаж всех товаров {total_sum}') 
    #         # print(f'Cреднее количество продаж всех товаров {total_sum/count}') 
    #         # print(count)


    # for phone in phones[0]:
    #     # sum_of_each += phone['items_sold']
    #     #product_count = phones['product']
    #     #print(phones['product'])
    #     print(phone)
    #     # for item in phone['items_sold']:
    #     #     total_sum += item
    #     #     count += 1
    #     #     # print(f'Суммарное количество продаж всех товаров {total_sum}') 
    #     #     # print(f'Cреднее количество продаж всех товаров {total_sum/count}') 
    #     #     # print(count)
    
    for phone in phones:
        # sum_of_each += phone['items_sold']
        product_name = phone['product']
        #print(phones['product'])
        # print(phone)
        product_item_sold = phones[count_product]['items_sold']
        
        # print(f'product_name {product_name}')
        # print(f'Каждый элемент списка (словарь): {phones[count_product]}')
        # print(f'Данные для количества: {product_item_sold}')
        # print(f'Тип данных для количества: {type(product_item_sold)}')

        sum_of_each = 0
        count_each = 0

        for item in product_item_sold:
            sum_of_each += item
            total_sum += item
            count += 1
        #     print(count_product)
        
        # res_dict['product'] = product_name
        # res_dict['total_sold'] = sum_of_each
        # res_dict['avg_sold'] = sum_of_each/len(product_item_sold)
        # print('счетчик: ', count_product)
        print(f'Суммарное количество продаж для {product_name}: {sum_of_each}')
        print(f'Cреднее количество продаж для {product_name}: {sum_of_each/len(product_item_sold)}')

        
        count_product += 1
    
    print(f'Суммарное количество продаж всех товаров {total_sum}') 
    print(f'Cреднее количество продаж всех товаров {total_sum/count}') 
        
        # for item in phone['items_sold']:
        #     total_sum += item
        #     count += 1
        #     # print(f'Суммарное количество продаж всех товаров {total_sum}') 
        #     # print(f'Cреднее количество продаж всех товаров {total_sum/count}') 
        #     # print(count)

    # print(f'Суммарное количество продаж всех товаров {total_sum}') 
    # print(f'Cреднее количество продаж всех товаров {total_sum/count}') 
    # for item in res_dict:
        # print(f'Суммарное количество продаж для {(res_dict['product'])} {(res_dict['total_sold'])}') 
        # print('Суммарное количество продаж для ',res_dict['product'],': ',res_dict['total_sold']) 
        # print(f'Cреднее количество продаж для {(res_dict['product'])} {(res_dict['avg_sold'])}') 

    # print(count)         
             
           
           
if __name__ == "__main__":
    main()
